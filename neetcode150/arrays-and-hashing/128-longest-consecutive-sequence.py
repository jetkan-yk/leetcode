class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in num_set:
                continue  # Not start of sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(length, longest)
        return longest


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().longestConsecutive)
    eval.add_case([100, 4, 200, 1, 3, 2], expected=4)
    eval.add_case([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], expected=9)
    eval.run()
