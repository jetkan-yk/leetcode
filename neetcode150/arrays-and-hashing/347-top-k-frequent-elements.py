import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap: list[int] = []
        counts = Counter(nums)
        for num, count in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            elif heap[0][0] < count:
                heapq.heapreplace(heap, (count, num))
        return [num for _, num in heap]


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().topKFrequent, verify=lambda x, y: sorted(x) == sorted(y))
    eval.add_case([1, 1, 1, 2, 2, 3], 2, expected=[1, 2])
    eval.add_case([1], 1, expected=[1])
    eval.run()
