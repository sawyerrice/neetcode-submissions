class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max = 0
        l = 0
        r = len(heights)-1
        while l < r:
            hl = heights[l]
            hr = heights[r]
            area = min(hl,hr)* (r-l)
            if area > max:
                max = area

            if hl > hr:
                r -=1
            else:
                l+=1

        return max

        