#Python3
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=sorted(stones,reverse=True)
        while(len(stones)>1):
            if(stones[0]==stones[1]):
                del stones[0:2]
            else:
                stones[0]=stones[0]-stones[1]
                del stones[1]
            stones=sorted(stones,reverse=True)
        if(len(stones)==1):
            return stones[0]
        else:
            return 0
