class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if len(s3) != m+n:
            return False
        dp = [False for _ in range(n+1)]
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m and j == n:
                    dp[j] = True
                elif i == m:
                    dp[j] = dp[j+1] and s2[j] == s3[i+j]
                elif j == n:
                    dp[j] = dp[j] and s1[i] == s3[i+j]
                else:
                    dp[j] = (dp[j+1] and s2[j] == s3[i+j]) or (dp[j] and s1[i] == s3[i+j])
            
        return dp[0]