class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().containsDuplicate)
    eval.add_case([1, 2, 3, 1], expected=True)
    eval.add_case([1, 2, 3, 4], expected=False)
    eval.add_case([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], expected=True)
    eval.run()
