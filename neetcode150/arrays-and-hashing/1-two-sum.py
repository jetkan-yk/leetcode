class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {num: idx for idx, num in enumerate(nums)}
        for idx, num in enumerate(nums):
            if (diff := target - num) in map and (idx2 := map[diff]) != idx:
                return [idx, idx2]


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().twoSum)
    eval.add_case(nums=[2, 7, 11, 15], target=9, expected=[0, 1])
    eval.add_case(nums=[3, 2, 4], target=6, expected=[1, 2])
    eval.add_case(nums=[3, 3], target=6, expected=[0, 1])
    eval.run()
