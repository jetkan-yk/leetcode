"""
Problem: https://leetcode.cn/problems/coin-change/
Difficulty: Medium

Solution #1: Top Down
- Time: O(num_coins ^ amount)
- Space: O(amount)

The subproblem branching factor is the number of coins, and the depth is the amount.

Solution #2: Top Down with Memoization
- Time: O(amount x num_coins)
- Space: O(amount)

Each subproblem is solved only once with memoization. There are O(amount) unique subproblems, and for each subproblem we iterate through all coins.

Solution #3: Bottom Up with Memoization
- Time: O(amount x num_coins)
- Space: O(amount)

The memo[i] represents the minimum number of coins needed to make amount i.
"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # return self.top_down_with_memo(coins, amount, [None] * (amount + 1))
        return self.bottom_up_with_memo(coins, amount)

    def top_down(self, coins: list[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        min_count = -1
        for coin in coins:
            count = self.top_down(coins, amount - coin) + 1
            if count == 0:
                continue
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
                continue
            if min_count == -1 or count < min_count:
                min_count = count

        memo[amount] = min_count
        return memo[amount]

    def bottom_up_with_memo(self, coins: list[int], amount: int) -> int:
        memo = [-1] * (amount + 1)
        memo[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0 or memo[i - coin] == -1:
                    continue
                count = memo[i - coin] + 1
                if memo[i] == -1 or count < memo[i]:
                    memo[i] = count
        return memo[amount]


if __name__ == "__main__":
    from leetcode import Evaluator

    eval = Evaluator(Solution().coinChange)
    eval.add_case(coins=[1, 2, 5], amount=11, expected=3)
    eval.add_case(coins=[2], amount=3, expected=-1)
    eval.add_case(coins=[1], amount=0, expected=0)
    eval.run()
