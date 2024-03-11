class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # dic key=no value=count loop -> max value
        d={}
        for n in nums:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        
        for k in d:
            if d[k]>1:
                return k
