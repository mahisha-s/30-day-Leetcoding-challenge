#Python3
#Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        initial=[nums[0]]
        a=[nums[0]]
        for i in range(1,len(nums)):
            if((sum(initial)+nums[i])>nums[i]):
                initial+=[nums[i]]
            else:
                initial=[nums[i]]
            a+=[sum(initial)]
        return max(a)
