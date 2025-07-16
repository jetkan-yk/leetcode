import operator
from itertools import accumulate


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Populate ans with suffix mul, then overwrite from left to right
        # with actual answer (prefix[i - 1] * suffix[i+1])
        ans = list(accumulate(reversed(nums), operator.mul))
        ans.reverse()

        prefix = 1
        for i, num in enumerate(nums):
            suffix = ans[i + 1] if i + 1 < len(nums) else 1
            ans[i] = prefix * suffix
            prefix = prefix * num
        return ans


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().productExceptSelf)
    eval.add_case([1, 2, 3, 4], expected=[24, 12, 8, 6])
    eval.add_case([-1, 1, 0, -3, 3], expected=[0, 0, 9, 0, 0])
    eval.run()
