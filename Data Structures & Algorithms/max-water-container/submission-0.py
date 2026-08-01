class Solution:
    def maxArea(self, heights: List[int]) -> int:
        z = 0
        y = len(heights) 
        x = y - 1
        maxArea = 0
        while x > z:
            if heights[x] >= heights[z]:           
                Area = heights[z] * (x - z)
                if Area > maxArea:
                    maxArea = Area
                z = z + 1

            else:
                Area = heights[x] * (x - z)
                if Area > maxArea:
                    maxArea = Area
                x = x - 1
        return maxArea
             
                  
#now I'm thinking if we have to loop, either we first maximise for either breadth or height
        









        













    


        