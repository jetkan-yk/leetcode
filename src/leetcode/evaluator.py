from typing import Any, Callable


def prettify(fn: Callable, args: tuple, kwargs: dict) -> str:
    arstrs = [str(x) for x in args]
    kwstrs = [f"{k}={v}" for k, v in kwargs.items()]
    return f"{fn.__name__}({', '.join(arstrs + kwstrs)})"


class Evaluator:
    def __init__(self, fn: Callable, verify: bool | Callable[[Any, Any], bool] = True):
        """
        Initialize an evaluator, `fn` is the leetcode function that evaluates the
        `output` of each test case.

        If `verify` is True, check each test case if the `output` == `expected`.

        If `verify` is False, print the `output` and `expected` values only.

        Alternatively, use a custom `verify` function that takes two positional
        arguments `output` & `expected` as input and return a boolean value indicating
        the test case has passed or failed.
        """

        def default_verify(output: Any, expected: Any) -> bool:
            return output == expected

        self.fn = fn
        self.verify = default_verify if verify is True else verify
        self.cases = []

    def add_case(self, *args, expected, **kwargs) -> None:
        """
        Add a new test case, the arguments can be in the form of positional or keyword
        args, which will be passed to the `fn` as-is for evaluation.

        Must contain a keyword-argument `expected` for the test case's expected output.
        """
        self.cases.append((args, kwargs, expected))

    def run(self) -> None:
        """
        Run the evaluation using all registered test cases.
        """
        show_ac = True
        for args, kwargs, expected in self.cases:
            print(f"Evaluating: {prettify(self.fn, args, kwargs)})")
            output = self.fn(*args, **kwargs)

            if self.verify is False or not self.verify(output, expected):
                print(f"Output: {output}\nExpected: {expected}\n")
                show_ac = False

        if show_ac:
            print("All correct!\n")
