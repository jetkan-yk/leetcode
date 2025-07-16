"""
Problem: https://leetcode.cn/problems/container-with-most-water/
Difficulty: Medium

Solution #1: Two Pointers
- Time: O(n)
- Space: O(1)

Use two pointers, one at the start and one at the end of the array.

At each step, calculate the area formed by the lines at the two pointers and the distance between them.

Update the maximum area found so far. Move the pointer pointing to the shorter line inward, as this will potentially increase the area in the next step.

This approach ensures that we explore all possible pairs of lines while maintaining an efficient time complexity.
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
