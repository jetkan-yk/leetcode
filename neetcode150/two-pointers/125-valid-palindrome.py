class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [c.lower() for c in s if c.isalnum()]
        i, j = 0, len(chars) - 1
        while i < j:
            if chars[i] != chars[j]:
                return False
            i += 1
            j -= 1
        return True

    def isPalindromeFast(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s.lower()))
        return s == s[::-1]


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().isPalindrome)
    eval.add_case("A man, a plan, a canal: Panama", expected=True)
    eval.add_case("race a car", expected=False)
    eval.add_case(" ", expected=True)
    eval.run()

    eval.fn = Solution().isPalindromeFast
    eval.run()
