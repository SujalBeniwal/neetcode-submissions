class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = []
        dic2 = []
        for char in s:
            dic1.append(char)
    
        for char in t:
            dic2.append(char)
        
        dic1.sort()
        dic2.sort()

        if dic1 == dic2: 
            return True
        else: return False

            


    

 