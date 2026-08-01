class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num2 = set()
        for x in nums:
            if x in num2:      
                return True    
            num2.add(x)
        
        return False

        
       
            
                

              

    
