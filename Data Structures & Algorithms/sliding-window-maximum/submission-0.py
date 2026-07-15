class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # Will store indices of elements
        result = []
    
        for i, num in enumerate(nums):
        # 1. Remove indices that are out of the current window bound
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
        # 2. Maintain monotonic decreasing property
        # Remove elements from back of deque that are smaller than the current element
            while dq and nums[dq[-1]] < num:
                dq.pop()
            
        # 3. Add current element's index to the deque
            dq.append(i)
        
        # 4. If window size has reached 'k', the front element is the max for this window
            if i >= k - 1:
                result.append(nums[dq[0]])
            
        return result