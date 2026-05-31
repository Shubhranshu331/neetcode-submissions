class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for i in range (len(nums)):
            if nums[i] in seen:
                return True
                break
            seen.add(nums[i])
        return False