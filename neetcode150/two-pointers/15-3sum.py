class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        ans = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if (sum := num + nums[l] + nums[r]) == 0:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return ans


if __name__ == "__main__":
    from leetcode import Evaluator

    def verify(output: list[list[int]], expected: list[list[int]]) -> bool:
        _output = sorted([sorted(s) for s in output])
        _expected = sorted([sorted(s) for s in expected])
        return _output == _expected

    eval = Evaluator(Solution().threeSum, verify=verify)
    eval.add_case([-1, 0, 1, 2, -1, -4], expected=[[-1, -1, 2], [-1, 0, 1]])
    eval.add_case([0, 1, 1], expected=[])
    eval.add_case([0, 0, 0], expected=[[0, 0, 0]])
    eval.run()
