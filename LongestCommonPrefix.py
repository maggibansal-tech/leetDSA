class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0 or len(strs[0])==0:
            return ""
        prefix=strs[0]
        for i in range(1,len(strs)):
            while (strs[i].startswith(prefix)==False):
                prefix=prefix[:-1]
        return prefix
                    
