import math
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2 = 0
        i3 = 0
        i5 = 0
        
        out = [1]
        while len(out)!= n:
            
            #Important
            A2,A3,A5 = out[i2]*2,out[i3]*3,out[i5]*5
            
            A = min(A2,A3,A5)   
            if A2== A: i2+=1
            if A3== A: i3+=1       
            if A5== A: i5+=1
                     
            out.append(A)
        return out[-1]
