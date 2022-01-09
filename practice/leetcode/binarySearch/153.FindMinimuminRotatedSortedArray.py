# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] <= nums[n - 1]:
            return nums[0]

        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                low = mid + 1
            else:
                high = mid - 1
        return nums[low]
