class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return all(arr[i - 2] - arr[i - 1] == arr[i - 1] - arr[i] for i in range(2, len(arr)))