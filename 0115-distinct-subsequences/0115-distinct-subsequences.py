class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n, m = len(s), len(t)
        
        # dp[i][j] = number of distinct subsequences of s[0..i-1] equal to t[0..j-1]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Base case: empty string t can always be matched in 1 way
        for i in range(n + 1):
            dp[i][0] = 1
            
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[n][m]
    
        