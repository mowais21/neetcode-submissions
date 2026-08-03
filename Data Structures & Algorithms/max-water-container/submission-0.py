class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # goal: we want to calculate the max area
        # constraint: don't know where the max would be
        # area = width * height = (r-l) * min(heights[l], heights[r]) 
        # key: start with the biggest width, calculate current area
        #      area would only increase if we are able to find a bigger length

        max_area = -1

        r = len(heights) - 1
        l = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(area, max_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
