def quick_sort(arr: list[int]) -> list[int]:
    if not arr:
        return []

    pivot = arr[0]
    left_arr = []
    right_arr = []

    for num in arr[1:]:
        if num < pivot:
            left_arr.append(num)
        else:
            right_arr.append(num)

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


if __name__ == "__main__":
    print()
    print(quick_sort([3, 2, 1, 5, 4]))
