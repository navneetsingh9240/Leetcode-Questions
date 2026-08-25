class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        for i in range(1,102):
            a=k*i
            if a not in nums:
                return a 

        
