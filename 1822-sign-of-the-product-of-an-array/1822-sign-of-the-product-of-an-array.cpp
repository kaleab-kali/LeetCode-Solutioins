class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        product = 1
        for i in nums:
            if i < 0:
                product *= -1
        return product