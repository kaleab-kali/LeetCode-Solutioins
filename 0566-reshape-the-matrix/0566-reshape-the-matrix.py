class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = sum(mat, [])
        if len(flat) != r * c:
            return mat
        tuples = zip(*([iter(flat)] * c))
        return map(list, tuples)