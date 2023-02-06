class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final = []
        for i in range(n):
            final.append(nums[i])
            final.append(nums[n+i])
        return final
        