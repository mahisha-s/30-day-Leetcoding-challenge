#Python3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=list(set(nums))
        l=[nums.count(i) for i in s]
        i=l.index(1)
        return s[i]
