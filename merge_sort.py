def merge_sort(arr):
    def merge(left, right):
        l, r = 0, 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        return result + left[l:] + right[r:]  # append leftover

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


arr = [5, 6, 4, 3, 2, 1]
assert [1, 2, 3, 4, 5, 6] == merge_sort(arr)
