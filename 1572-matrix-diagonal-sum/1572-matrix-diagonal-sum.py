class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        return sum(sum(r[j] for j in {i, len(r) - i - 1}) for i, r in enumerate(mat))