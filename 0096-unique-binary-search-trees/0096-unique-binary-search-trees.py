class Solution:
    def numTrees(self, n: int) -> int:
        # return self.catalanNumber(n)
        return self.dp(n)

    def dp(self, n):
        dp = [0 for _ in range(n+1)]
        # if there is no node to build tree, it is None therefore only 1 possibility.
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
    
    def catalanNumber(self, n):
        c = 1
        for i in range(n):
            c = c * 2 * (2 * i + 1) / (i + 2)
        return int(c)