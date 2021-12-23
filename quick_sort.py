from __future__ import annotations


def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    piv = arr[0]
    others = arr[1:]

    left = [v for v in others if v <= piv]
    right = [v for v in others if v > piv]
    return quick_sort(left) + [piv] + quick_sort(right)


if __name__ == "__main__":
    arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    result = quick_sort(arr)
    assert result == list(range(10))
