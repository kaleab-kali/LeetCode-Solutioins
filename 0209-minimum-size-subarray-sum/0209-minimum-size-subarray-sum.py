class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curSum = 0
        minLen = float('inf')
        for r in range(len(nums)):
			# add to curSum
            curSum += nums[r]
            while curSum >= target and l <= r:
				# update minlen
                minLen = min(minLen, (r - l)+1)
				# minlen ever hits 1, just return 1
                if minLen == 1:
                    return 1
				# update cursum and l pointer
                curSum -= nums[l]
                l += 1
        return minLen if minLen != float('inf') else 0