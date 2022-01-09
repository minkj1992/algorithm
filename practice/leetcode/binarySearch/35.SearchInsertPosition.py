# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0

        high = len(nums) - 1
        low = 0

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return high + 1  # = low -1


def searchInsert(nums: List[int], target: int) -> int:
    if target <= nums[0]:
        return 0

    high = len(nums) - 1
    low = 0

    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print(low, mid, high)
    return high + 1  # == low


nums = [
    0,
]
target = 9
assert searchInsert(nums, target) == 1
