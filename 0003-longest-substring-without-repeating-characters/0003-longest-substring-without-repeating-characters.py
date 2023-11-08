class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #brute force -> keep two for loop cj=heck if they dont match then to res
        #sliding window -> keep mkving until encountered duplicate using set then pop length will be maintained
        charset=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res=max(res,r-l+1)
        return res
