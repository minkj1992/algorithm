"""
https://leetcode.com/problems/top-k-frequent-elements/
"""
from collections import Counter


# Counter 방법
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return sorted(counter.keys(), key=counter.get, reverse=True)[:k]
