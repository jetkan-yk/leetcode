"""
Problem: https://leetcode.cn/problems/coin-change/
Difficulty: Medium

Solution #1: Top Down with Memoization
- Time: O(amount x len(coins))
- Space: O(amount)

Uses top down recursion with memoization: min(count(amount - coin) + 1 for each coin)
"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        return self.top_down_with_memo(coins, amount, [None] * (amount + 1))

    def top_down(self, coins: list[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        min_count = -1
        for coin in coins:
            count = self.top_down(coins, amount - coin) + 1
            if count == 0:
                continue  # Skip if no solution for this coin
            if min_count == -1 or count < min_count:
                min_count = count
        return min_count

    def top_down_with_memo(self, coins: list[int], amount: int, memo: list[int | None]) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if memo[amount] is not None:
            return memo[amount]

        min_count = -1
        for coin in coins:
            count = self.top_down_with_memo(coins, amount - coin, memo) + 1
            if count == 0:
                continue  # Skip if no solution for this coin
            if min_count == -1 or count < min_count:
                min_count = count

        memo[amount] = min_count
        return memo[amount]


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().coinChange)
    eval.add_case(coins=[1, 2, 5], amount=11, expected=3)
    eval.add_case(coins=[2], amount=3, expected=-1)
    eval.add_case(coins=[1], amount=0, expected=0)
    eval.run()
