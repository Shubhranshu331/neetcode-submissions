class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left =0 
        right = len(heights)-1
        max_water=0
        while left<right:
            width=right-left
            current_height=min(heights[left],heights[right])
            current_area=current_height*width
            max_water=max(max_water,current_area)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_water