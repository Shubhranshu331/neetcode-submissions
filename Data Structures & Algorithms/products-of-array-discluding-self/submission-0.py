class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range (len(nums)):
            j=0
            prefix =1
            postfix=1
            while j<i:
                prefix=prefix*nums[j]
                j+=1
            j=i+1
            while j<len(nums):
                postfix=postfix*nums[j]
                j+=1

            res.append(prefix*postfix)
        return res

            