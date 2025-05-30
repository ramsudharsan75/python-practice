"""Posts Router"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from app import database, models, schemas
from app.oauth2 import get_current_user

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/", response_model=list[schemas.PostVoteOut])
def get_posts(
    db_session: Session = Depends(database.get_db),
    current_user=Depends(get_current_user),
    limit: int = 10,
    skip: int = 0,
    search: str = "",
):
    """Get Posts Route"""
    posts_with_votes = (
        db_session.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.title.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )
    return posts_with_votes


@router.get("/{post_id}", response_model=schemas.PostVoteOut)
def get_post(post_id: int, db_session: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    """Get Post Route"""
    post = (
        db_session.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .group_by(models.Post.id)
        .filter(models.Post.id == post_id)
        .first()
    )

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {post_id} was not found")

    return post


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostOut)
def create_post(
    post: schemas.CreatePost,
    db_session: Session = Depends(database.get_db),
    current_user=Depends(get_current_user),
):
    """Create Post Route"""

    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db_session.add(new_post)
    db_session.commit()
    db_session.refresh(new_post)
    return new_post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db_session: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    """Delete Post Route"""
    post_query = db_session.query(models.Post).filter(models.Post.id == post_id)

    post_to_delete = post_query.first()

    if not post_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {post_id} was not found")

    if post_to_delete.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform delete operation")

    post_query.delete(synchronize_session=False)
    db_session.commit()


@router.put("/{post_id}", status_code=status.HTTP_201_CREATED, response_model=schemas.PostOut)
def update_post(
    post_id: int,
    post_update: schemas.UpdatePost,
    db_session: Session = Depends(database.get_db),
    current_user=Depends(get_current_user),
):
    """Update Post Route"""
    post_query = db_session.query(models.Post).filter(models.Post.id == post_id)
    post_to_update = post_query.first()

    if not post_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {post_id} was not found")

    if post_to_update.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform update operation")

    updated_post = {getattr(models.Post, key): value for key, value in post_update.dict().items()}

    post_query.update(updated_post, synchronize_session=False)
    db_session.commit()
    return post_query.first()
