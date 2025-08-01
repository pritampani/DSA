class Solution:
    def minCoins(self, coins, sum):
        # code here
        res = self.minCoinsutil(coins, 0, sum)
        return res if res != float('inf') else -1

    def minCoinsutil(self, coins, i, sum):

        # base case
        if sum == 0:
            return 0
        if i >= len(coins) or sum < 0:
            return float('inf')

        # exclude
        a = self.minCoinsutil(coins, i + 1, sum)
        b = float('inf')
        if coins[i] <= sum:
            b = 1 + self.minCoinsutil(coins, i, sum - coins[i])

        return min(a, b)

sol = Solution()
print(sol.minCoins([1, 2, 5], 11))