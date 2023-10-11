"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

init : 0,0
대소 비교: (i + 1, j) vs (i, j+1)를 비교해서 heap에 넣어주어야 한다.
예를 들어 nums1 = [1,1,1,1,1,1,1,1,1], nums2 = [1,2,3,4,5] , k = 3

result = [[1,1],[1,1],[1,1]]
"""

import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)

        if n == 0 or m == 0 or k == 0:
            return []

        heap = [(nums1[0] + nums2[0], 0, 0)]
        pairs = []
        visited = {}
        while heap and len(pairs) < k:
            print(heap)
            _, i, j = heapq.heappop(heap)
            pairs.append([nums1[i], nums2[j]])
            for ni, nj in ((i + 1, j), (i, j + 1)):
                if visited.get((ni, nj), False) or ni >= n or nj >= m:
                    continue
                visited[(ni, nj)] = True
                heapq.heappush(heap, (nums1[ni] + nums2[nj], ni, nj))
        print(heap)
        return pairs


if __name__ == "__main__":
    s = Solution()
    result = s.kSmallestPairs([1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 3], 3)
    assert result == [[1, 1], [1, 1], [1, 1]]
