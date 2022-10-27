class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [(len([i for i in nums if i < digit])) for digit in nums]   
        