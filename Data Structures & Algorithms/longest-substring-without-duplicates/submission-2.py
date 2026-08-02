class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = {}
        right_pointer = 0
        left_pointer = 0 
        x = ""
        counter = 0
        max_counter = 0
        for i in range(len(s)):
            x = s[i]
            if x in dictionary:
                left_pointer = max(left_pointer, dictionary[x] +1)
                dictionary[x] = i
             
            else:
                dictionary.update({x:i})
            right_pointer = i

            counter = right_pointer - left_pointer + 1
            if max_counter < counter:
                max_counter = counter

        return max_counter
        