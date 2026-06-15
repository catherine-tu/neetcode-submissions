class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # approach: DP: accumulate sum of left & top
        dp = [[1] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # bc: if at 0, 0 -- one sol
                if i == 0 and j == 0:
                    continue
                # if at row 0: only count lefts -- only way to reach
                elif i == 0:
                    dp[i][j] = dp[i][j-1] 
                # if at col 0: only count aboves -- only way to reach
                elif j == 0:
                    dp[i][j] = dp[i-1][j] 
                # otherwise, count both - both ways can reach
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] 
        return dp[m-1][n-1]