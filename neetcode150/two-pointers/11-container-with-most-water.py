"""
Problem: https://leetcode.cn/problems/container-with-most-water/
Difficulty: Medium

Solution #1: Two Pointers
- Time: O(n)
- Space: O(1)

Use two pointers starting at opposite ends of the array to find the maximum water container area.

Algorithm:
1. Initialize left pointer at start (0) and right pointer at end (n-1) for maximum width
2. Calculate area: width x min(height[left], height[right])
3. Move the pointer at the shorter line inward, as keeping it would only yield smaller areas
4. Repeat until pointers meet

Key insight: Moving the shorter line pointer eliminates all suboptimal containers that use
that line with smaller widths, ensuring we find the optimal solution without checking all O(n²) pairs.
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(area, max_area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return max_area


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().maxArea)
    eval.add_case([1, 8, 6, 2, 5, 4, 8, 3, 7], expected=49)
    eval.add_case([1, 1], expected=1)
    eval.run()
