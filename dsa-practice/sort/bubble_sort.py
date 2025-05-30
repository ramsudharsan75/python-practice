"""Bubble sort algorithm implementation."""


def bubble_sort_in_place(arr: list[int]) -> None:
    """Sorts the array in place using bubble sort algorithm."""
    n = len(arr)

    for i in range(n, 0, -1):
        for j in range(1, i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]


if __name__ == "__main__":
    lst = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort_in_place(lst)
    print("Sorted array is:", lst)
