class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
#     other solution
        # nums = [str(x) for x in nums]
        # nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
        # return ''.join(nums).lstrip('0') or '0'