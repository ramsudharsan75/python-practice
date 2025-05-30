def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    i = j = 0
    sorted_arr = []

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            j += 1

    sorted_arr += left_arr[i:]
    sorted_arr += right_arr[j:]
    return sorted_arr


if __name__ == "__main__":
    print(merge_sort([3, 2, 1, 5, 4]))  # Output: [1, 2, 3, 4, 5]
