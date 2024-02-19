class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        e=None
        for i in range(n):
            if c==0:
                e=nums[i]
                c+=1
            elif nums[i]==e:
                c+=1
            else:
                c-=1
        c1=0
        for i in range(n):
            if nums[i]==e:
                c1+=1
        if c1 > (n / 2):
            return e
        return -1