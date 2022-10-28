class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red,white=nums.count(0),nums.count(1)
        for i in range(len(nums)):
            if red != 0:
                nums[i]=0
                red -= 1
            elif white !=0:
                nums[i]=1
                white -= 1
            else:
                nums[i]=2
       
                