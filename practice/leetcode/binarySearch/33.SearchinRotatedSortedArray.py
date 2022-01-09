# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def get_result(i):
            return i if nums[i] == target else -1

        n = len(nums)
        if n == 1:
            return get_result(0)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid - 1] > nums[mid]:
                return get_result(mid)
            if nums[mid] > nums[mid + 1]:
                return get_result(mid + 1)

            if nums[0] > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1


nums = [1, 3]
s = Solution()
result = s.search(nums, 3)
print(result)
