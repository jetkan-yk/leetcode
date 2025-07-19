"""
Problem: https://leetcode.cn/problems/climbing-stairs/
Difficulty: Easy

Solution #1: Dynamic Programming
- Time: O(n)
- Space: O(1)

Iteratively calculate the number of ways to reach each step using the previous two steps: step n = step n-1 + step n-2
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev_1, prev_2, curr = 1, 2, 0
        for _ in range(2, n):
            curr = prev_1 + prev_2
            prev_1, prev_2 = prev_2, curr
        return curr


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().climbStairs)
    eval.add_case(1, expected=1)
    eval.add_case(2, expected=2)
    eval.add_case(3, expected=3)
    eval.run()
