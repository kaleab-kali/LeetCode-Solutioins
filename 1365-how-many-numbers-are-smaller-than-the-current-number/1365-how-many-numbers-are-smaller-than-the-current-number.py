class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [*map(sorted(nums).index, nums)]
        