class Solution:
    def digitsum(self,num):
        cnt = 0
        while num !=0:
            cnt+=num%10
            num = num//10
        
        return cnt
    
    def isUgly(self,num):
        if num==1:
            return 1
        elif num<=0:
            return 0
        else:
            if num%10==0:
                return self.isUgly(num//10)
            elif num%10 ==5:
                return self.isUgly(num//5)
            elif self.digitsum(num)%9==0:
                return self.isUgly(num//9)
            elif self.digitsum(num)%3==0:
                return self.isUgly(num//3)
            elif num%4 ==0:
                return self.isUgly(num//4)
            elif num%2 ==0:
                return self.isUgly(num//2)
            else:
                return num==1
