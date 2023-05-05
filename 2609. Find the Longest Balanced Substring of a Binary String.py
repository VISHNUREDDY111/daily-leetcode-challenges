class Solution:
    def isbalanced(self,l,r,s):
        while l>=0 and r<len(s) and s[l]=='0' and s[r]=='1':
            l-=1
            r+=1
        return r-l-1

    def findTheLongestBalancedSubstring(self, s: str) -> int:
        if "01" not in s:
            return 0
        maxres=0
        for i in range(len(s)):
            res=self.isbalanced(i,i+1,s)
            maxres=max(maxres,res)
        return maxres 
