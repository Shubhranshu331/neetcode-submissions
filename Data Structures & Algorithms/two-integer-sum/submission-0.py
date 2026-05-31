class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            need= target-num
            if need in dict:
                return [dict[need],i]

            dict[num]=i