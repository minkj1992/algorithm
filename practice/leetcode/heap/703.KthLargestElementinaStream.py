"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Time complexity = O( n*log(n) + m*log(k) )
heap을 사용하게 되면 느슨하게 sorted된 상태를 유지 할 수 있다. 
그러므로 k th largest number의 상태가 계속 진행되면서 추가된다면 heap을 사용하는 것이 현명하다.
왜냐하면 quick sort는 O(n log n)이지만, add()함수가 호출 될때마다 sort를 다시 해주어야 하지만,
heap의 경우에는 priority queue에 k size만 유지하면 max kth element를 root로 가질 수 있다.
"""

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap: List[int] = nums
        self.init_heap()

    def init_heap(self):
        n = len(self.heap)
        heapq.heapify(self.heap)  # O (n/2 * log n)
        for _ in range(n - self.k):
            heapq.heappop(self.heap)

    @property
    def kth_element(self):
        """
        M = number of add calls
        O(M * log K)
        """
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        return self.kth_element
