class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        suf=[0]*n
        suf[-1]=nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i]=min(suf[i + 1],nums[i])  
        max_so_far=0
        for i in range(n):
            max_so_far=max(max_so_far, nums[i])
            if max_so_far - suf[i]<=k:
                return i  
        return -1
        