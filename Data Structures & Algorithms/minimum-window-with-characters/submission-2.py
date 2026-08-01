class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic1 = {}
        dic2 = {}
        left_pointer = ""
        right_pointer = ""
        for char in t:
            dic1[char] = 1 + dic1.get(char, 0)
        need = len(dic1)
        have = 0
        #we've built the map
        i = 0
        x = 0
        coord1 = 0
        coord2 = 0
        distance = float('inf')
        char1 = ""
        char2 = ""

        for i in range(len(s)):
            right_pointer = s[i]
            char1 = s[i]
            if dic1.get(char1) != None:
                dic2[char1] = 1 + dic2.get(char1,0)
                if dic2.get(char1) == dic1.get(char1):
                    have +=1
            else:
                    i += 1
            while have == need:
                char2 = s[x]
                if dic1.get(char2) != None:
                    if dic2.get(char2) <= dic1.get(char2):
                        have -= 1
                    dic2[char2] -= 1
                    if distance > i - x:
                        distance = i - x
                        coord1 = i
                        coord2 = x  
                else:
                    left_pointer = s[x]
                x += 1

        if distance != float('inf'):
            return s[coord2 : coord1 + 1]
        else:
            return ""

                
                    


                
            




    