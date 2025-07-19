"""
Problem: https://leetcode.cn/problems/climbing-stairs/
Difficulty: Easy

Solution #1: Dynamic Programming (array)
- Time: O(n)
- Space: O(n)

Iteratively calculate the number of ways to reach each step x using f(x) = f(x-1) + f(x-2).

Solution #2: Dynamic Programming (variables)
- Time: O(n)
- Space: O(1)

At each step, only the last two computed values are needed, so we can use two variables to keep track of them instead of an entire array.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.array(n)
        return self.variables(n)

    def array(self, n: int) -> int:
        if n < 3:
            return n

        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    def variables(self, n: int) -> int:
        if n < 3:
            return n

        prev_1, prev_2 = 1, 2
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
    eval.add_case(4, expected=5)
    eval.run()
