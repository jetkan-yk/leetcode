"""
Problem: https://leetcode.cn/problems/trapping-rain-water/
Difficulty: Hard

Solution #1: Dynamic Programming
- Time: O(n)
- Space: O(n)

The dynamic programming approach pre-computes the maximum height to the left and right of each position.
For each position, the water level is determined by the minimum of the maximum heights on both sides.
The amount of water trapped at each position is the difference between this water level and the height at that position.
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        return self.dp(height)

    def dp(self, height: list[int]) -> int:
        if len(height) < 3:
            return 0

        max_left = [0] * len(height)
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        max_right = [0] * len(height)
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        area = 0
        for i in range(len(height)):
            area += max(min(max_left[i], max_right[i]) - height[i], 0)
        return area


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().trap)
    eval.add_case([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], expected=6)
    eval.add_case([4, 2, 0, 3, 2, 5], expected=9)
    eval.run()
