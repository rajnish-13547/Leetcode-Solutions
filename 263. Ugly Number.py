class Solution:      
        
    def isUgly(self, num) -> bool:
        def divide(N=1):
            if N<=0:
                return 0
            elif N ==1: 
                return 1
            elif N ==2 or N ==3 or N ==5:
                return 1
        
            A = str(N)
            val = 0
            for x in A:
                val +=int(x)
        
            if A[-1]=='5' or A[-1]=='0':
                return divide(int(N/5))
            elif int(A[-1])%2==0:
                return  divide(int(N/2))
            elif val%3==0:
                return divide(int(N/3))
            else:
                return N
        
        if divide(num)==1:
            return True
        else:
            return False
        
