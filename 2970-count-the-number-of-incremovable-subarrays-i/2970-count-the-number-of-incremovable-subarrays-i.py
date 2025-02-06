class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0 
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                flag= True
                last = -1
                for k in range(len(nums)):
                    if i <= k <= j:
                        continue 
                    else:
                        flag&= last < nums[k]
                        last = nums[k]
                ans+= int(flag)
        return ans 
                