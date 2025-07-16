class Codec:
    """
    Use first 3 digits to encode string length: <length:03d><s>
    e.g. ["Hello", "World!"] -> "005Hello006World!"
                                 ^  ^    ^
                                 i  j    j+size
    """

    def encode(self, strs: list[str]) -> str:
        return "".join([f"{len(s):03d}{s}" for s in strs])

    def decode(self, s: str) -> list[str]:
        i = 0
        ans = []
        while i < len(s):
            j = i + 3
            size = int(s[i:j])
            ans.append(s[j : j + size])
            i = j + size
        return ans


if __name__ == "__main__":
    from leetcode import Evaluator

    codec = Codec()
    eval = Evaluator(lambda s: codec.decode(codec.encode(s)))
    eval.add_case(["Hello", "World"], expected=["Hello", "World"])
    eval.add_case([""], expected=[""])
    eval.run()
