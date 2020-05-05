#Python3
#Week 1 Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        c=0
        while(n!=1 and c<10):
            m=list(map(int,list(str(n))))
            s=[i*i for i in m]
            n=sum(s)
            c+=1
        if(n==1):
            return True
        else:
            return False