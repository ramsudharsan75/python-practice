"""Votes Router"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import database, models, schemas
from app.oauth2 import get_current_user

router = APIRouter(prefix="/votes", tags=["Votes"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(
    vote: schemas.Vote,
    db_session: Session = Depends(database.get_db),
    current_user=Depends(get_current_user),
):
    """Create Vote Route"""

    post = db_session.query(models.Post.id == vote.post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {vote.post_id} does not exist")

    vote_query = db_session.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id
    )
    found_vote = vote_query.first()

    if vote.direction == 1:
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User {current_user.id} has already voted on post {vote.post_id}",
            )

        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db_session.add(new_vote)
        db_session.commit()
        return {"message": "Successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")

        vote_query.delete(synchronize_session=False)
        db_session.commit()

        return {"message": "Successfully deleted vote"}
