class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        newlist = sorted(nums)
        res = []
        for index,data in enumerate(newlist):
            if data == target:
                res.append(index)
            if data > target:
                break
        return res
                