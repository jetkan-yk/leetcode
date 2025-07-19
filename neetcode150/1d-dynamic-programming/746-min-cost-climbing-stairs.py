"""
Problem: https://leetcode.cn/problems/min-cost-climbing-stairs/
Difficulty: Easy

Solution #1: Dynamic Programming (array)
- Time: O(n)
- Space: O(n)

Iteratively calculate the minimal cost to reach each step x using f(x) = min(f(x-1) + f(x-2)) + cost(x).

Solution #2: Dynamic Programming (variable)
- Time: O(n)
- Space: O(1)

At each step, only the last two computed values are needed, so we can use two variables to keep track of them instead of an entire array.
"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # return self.array(cost)
        return self.variable(cost)

    def array(self, cost: list[int]) -> int:
        if len(cost) < 3:
            return min(cost)

        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[-1], dp[-2])

    def variable(self, cost: list[int]) -> int:
        if len(cost) < 3:
            return min(cost)

        prev_1, prev_2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            curr = min(prev_1, prev_2) + cost[i]
            prev_1, prev_2 = prev_2, curr
        return min(prev_1, prev_2)


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().minCostClimbingStairs)
    eval.add_case([10, 15, 20], expected=15)
    eval.add_case([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], expected=6)
    eval.run()
