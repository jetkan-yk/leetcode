"""
Problem: https://leetcode.cn/problems/daily-temperatures/
Difficulty: Medium

Solution #1: Monotonic Stack
- Time: O(n)
- Space: O(n)

We use a monotonic stack to keep track of indices of temperatures waiting to observe a warmer day.

When we observe a day that is warmer than the temperature in the stack, we have found the answer.

By maintaining the stack in decreasing order of temperatures, we can stop popping the stack when the temperature is higher.

This reduces the need to check all previous temperatures from O(n^2) to O(n).
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans, obs = [0] * len(temperatures), []
        for i, temp in enumerate(temperatures):
            while obs and temp > temperatures[obs[-1]]:
                ans[obs[-1]] = i - obs[-1]
                obs.pop()
            obs.append(i)
        return ans


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().dailyTemperatures)
    eval.add_case([73, 74, 75, 71, 69, 72, 76, 73], expected=[1, 1, 4, 2, 1, 1, 0, 0])
    eval.add_case([30, 40, 50, 60], expected=[1, 1, 1, 0])
    eval.add_case([30, 60, 90], expected=[1, 1, 0])
    eval.run()
