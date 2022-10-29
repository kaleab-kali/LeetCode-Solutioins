import statistics
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return statistics.mean(salary[1:-1])