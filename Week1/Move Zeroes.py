#Python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=nums.count(0)
        try:
            while True:
                nums.remove(0)
        except:
            pass
        nums+=[0 for i in range(n)]
