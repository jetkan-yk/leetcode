from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord("a")] += 1
            ans[tuple(counts)].append(s)  # Using count as key
        return list(ans.values())

    def groupAnagramsFast(self, strs: list[str]) -> list[list[str]]:
        PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

        def get_hash(s: str) -> int:
            ans = 1
            for c in s:
                ans *= PRIMES[ord(c) - ord("a")]
            return ans

        ans = defaultdict(list)
        for s in strs:
            ans[get_hash(s)].append(s)  # Using custom prime-based hash value as key
        return list(ans.values())


if __name__ == "__main__":
    from leetcode import Evaluator

    def verify(output: list[list[str]], expected: list[list[str]]) -> bool:
        _output = sorted([sorted(s) for s in output])
        _expected = sorted([sorted(s) for s in expected])
        return _output == _expected

    eval = Evaluator(Solution().groupAnagrams, verify=verify)
    eval.add_case(
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        expected=[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    )
    eval.add_case([""], expected=[[""]])
    eval.add_case(["a"], expected=[["a"]])
    eval.run()

    eval.fn = Solution().groupAnagramsFast
    eval.run()
