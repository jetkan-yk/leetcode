"""
Problem: https://leetcode.cn/problems/trapping-rain-water/
Tags:
Difficulty: Hard
Time: O()
Space: O()
Solution:
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        pass


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().trap)
    eval.add_case([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], expected=6)
    eval.add_case([4, 2, 0, 3, 2, 5], expected=9)
    eval.run()
