class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         L = []
         strt2 = {}
         for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))

            if strt2.get(sorted_word) == None:
                L.append([strs[i]])
                strt2[sorted_word] = len(L) - 1
            else:
                x = strt2.get(sorted_word)
                L[x].append(strs[i])
         return L






        #though we obviously need to print out the nonsorted elements, so let's put all the sorted elements in a dictionary with the same index




    
        