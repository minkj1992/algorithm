from typing import Optional, List


def binary_search(arr: List, target: int, start: int, end: int, is_sorted: bool = True) -> Optional[int]:
    """
    1. fail fast
    2. find mid
    3. if target find return 
    """

    if not is_sorted:
        print("arr must be sorted")
        return binary_search(sorted(arr), target, start, end)

    if start >= end:
        return False

    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    return binary_search(arr, target, mid+1, end)


if __name__ == "__main__":
    # binary se
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    unsorted_arr = [11, 13, 15, 17, 19, 1, 3, 5, 7, 9]
    n = len(arr)

    assert binary_search(unsorted_arr,
                         target=10,
                         start=0,
                         end=n - 1,
                         is_sorted=False) is False
    assert binary_search(arr, target=10, start=0, end=n-1) is False
    assert binary_search(arr, target=17, start=0, end=n-1) is True
