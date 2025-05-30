"""Insertion sort algorithm implementation."""


def insertion_sort_in_place(arr: list[int]) -> None:
    """Sorts the array in place using insertion sort algorithm."""
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    lst = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort_in_place(lst)
    print("Sorted array is:", lst)
