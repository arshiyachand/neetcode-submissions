class Solution:
    def maxArea(self, heights: List[int]) -> int:
        firstpointer = 0
        lastpointer = len(heights)-1 
        distance = len(heights)-1 
        area = 0

        while firstpointer < lastpointer:
            area = max(area, min(heights[firstpointer], heights[lastpointer])*distance)
            if heights[firstpointer] < heights[lastpointer]:
                firstpointer += 1
            else:
                lastpointer -= 1
            distance -= 1
        return area
        