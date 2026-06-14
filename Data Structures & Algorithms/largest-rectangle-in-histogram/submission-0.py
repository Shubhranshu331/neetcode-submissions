class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        max_area=0
        stack=[]
        for i in range(n+1):
            current_height = heights[i] if i<n else 0
            while stack and heights[stack[-1]]>=current_height:
                height=heights[stack.pop()]
                width = i if not stack else i-stack[-1]-1
                max_area = max(max_area,height*width)

            stack.append(i)
        return max_area