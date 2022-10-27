class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if(nums[i] > nums[j]):
                    counter += 1
            res.append(counter) 
        return res
        