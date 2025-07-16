class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1
        while True:
            if (sum := numbers[i] + numbers[j]) == target:
                return [i + 1, j + 1]
            elif sum < target:
                i += 1
            else:
                j -= 1


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().twoSum)
    eval.add_case([2, 7, 11, 15], 9, expected=[1, 2])
    eval.add_case([2, 3, 4], 6, expected=[1, 3])
    eval.add_case([-1, 0], -1, expected=[1, 2])
    eval.run()
