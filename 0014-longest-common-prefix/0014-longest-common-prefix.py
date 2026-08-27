class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        first,last=strs[0],strs[-1]    
        for i in range(min(len(first),len(last))):
            if first[i]!= last[i]:
                return first[:i]
        return first        

        