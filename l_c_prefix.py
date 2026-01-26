

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       if not strs:
        return ""
       
       strs.sort()
       new =[]
       first = strs[0]
       last = strs[-1]
       a = len(first)
       b = len(last)
       val = min(a,b)
       for i in range(val):

        if(first[i]==last[i]):
            new.append(first[i])
        else:
            break
       return "".join(new)
        
        


        
        
