class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if  x < 0 or (x%10==0 and x!=0):
            return False

        a=0
        while x > a:
            a=a*10+x%10
            x//=10

        return x==a or x==a//10           
        