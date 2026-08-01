class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        i = 0
        left_max = []
        right_max = []
        clipboardleft = 0
        clipboardright = 0

        for i in range(len(height)):
            if height[i] > clipboardleft:
                clipboardleft = height[i]
            left_max.append(clipboardleft)

        for i in reversed(range(len(height))):
            if height[i] > clipboardright:
                clipboardright = height[i]
            right_max.append(clipboardright)
        right_max.reverse()

        while i < len(height):
            if left_max[i] >= right_max[i]:
                difference = right_max[i] - height[i]
                if difference < 0:
                    difference = 0
                else:
                    output += difference
                i += 1
            else:
                difference = left_max[i] - height[i]
                if difference < 0:
                    difference = 0
                else:
                    output += difference
                i += 1
        return output

        

    
        