class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr,maximum=0,0
        for i in range(len(nums)):
            if nums[i]==1: 
                curr+=1
            else:
                curr=0
            maximum = max(curr,maximum)
        return maximum