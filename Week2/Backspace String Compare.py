#Python3
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s=list(S)
        t=list(T)
        while('#' in s):
            ind=s.index("#")
            if(ind==0):
                del s[ind]
            else:
                del s[ind-1:ind+1]
        while('#' in t):
            ind=t.index("#")
            if(ind==0):
                del t[ind]
            else:
                del t[ind-1:ind+1]
        print(s,t)
        if(s==t):
            return True
        else:
            return False
