# O(N)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        dp = [0]*n
        dp[0]=grid[0][0]
        for i in range(1, n):
            dp[i] = grid[0][i] + dp[i-1]

        for row in grid[1:]:
            for j in range(n):
                if j>0: dp[j] = row[j] + min(dp[j], dp[j-1])
                else: dp[j] += row[j]
        return dp[n-1]  