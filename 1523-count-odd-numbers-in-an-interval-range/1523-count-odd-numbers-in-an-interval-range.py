class Solution:
    def countOdds(self, low: int, high: int) -> int:
#         count = 0
#         for i in range(low, high+1):
#             if i % 2 != 0:
#                 count += 1
            
#         return count
        # return len([i for i in range(low, high+1) if i % 2 != 0])
        return (high + 1) // 2 - low // 2