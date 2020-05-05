#Python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=0
        profit=0
        n=len(prices)
        i=0
        while(i<n-1):
            while(i<n-1 and prices[i]>=prices[i+1]):
                i+=1
            if(i==n-1):
                break
            buy=prices[i]
            while(i<n-1 and prices[i]<prices[i+1]):
                i+=1
            sell=prices[i]
            profit+=(sell-buy)
        return profit
