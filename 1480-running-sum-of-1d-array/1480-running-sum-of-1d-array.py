class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # finalSum = [0] * len(nums)
        # finalSum[0] = nums[0]
        for i in range(1,len(nums)):
                # print(i)
                # finalSum[i] = nums[i] + finalSum[i-1]
                nums[i] += nums[i-1]

                # print(sum[i])
                
        return nums
            