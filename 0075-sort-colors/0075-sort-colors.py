class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        interval = len(nums) // 2
        while interval > 0:
            for i in range(interval, len(nums)):
                temp = nums[i]
                j = i
                while j >= interval and nums[j - interval] > temp:
                    nums[j] = nums[j - interval]
                    j -= interval

                nums[j] = temp
            interval //= 2
       
                