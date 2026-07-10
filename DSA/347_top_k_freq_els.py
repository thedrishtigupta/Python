

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        arr = freq.most_common(k)
        ans = [x for x, cnt in arr]

        return ans

# Heap
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [(-val, key) for key, val in freq.items()]

        heapq.heapify(heap)

        res = []

        for _ in range(k):
            val, key = heapq.heappop(heap)
            res.append(key)
        return res