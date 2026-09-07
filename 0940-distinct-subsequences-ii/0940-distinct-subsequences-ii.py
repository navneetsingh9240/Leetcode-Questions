class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 1000000007
        dp = 1
        last = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            old_dp = dp
            dp = (2 * dp - last[index] + MOD) % MOD
            last[index] = old_dp
        return (dp - 1 + MOD) % MOD