from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().isAnagram)
    eval.add_case("anagram", "nagaram", expected=True)
    eval.add_case("rat", "car", expected=False)
    eval.run()
