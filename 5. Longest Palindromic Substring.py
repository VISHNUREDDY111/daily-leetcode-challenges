class Solution:
    def isPalindrome(self,l,r,s):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return r-l-1
    def longestPalindrome(self, s: str) -> str:
        leng=0
        start=0
        end=0
        for i in range(len(s)):
            len1 = self.isPalindrome(i,i,s)
            len2 = self.isPalindrome(i,i+1,s)
            leng = max(len1, len2)
            if leng > end-start:
                start=i-(leng-1)//2
                end=i+leng//2
        return s[start:end+1]
