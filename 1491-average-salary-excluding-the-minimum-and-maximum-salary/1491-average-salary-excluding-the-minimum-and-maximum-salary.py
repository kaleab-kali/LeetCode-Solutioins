# import statistics
class Solution:
    def average(self, salary: List[int]) -> float:
        # salary.sort()
        # return statistics.mean(salary[1:-1])
        salary.pop(salary.index(min(salary)))
        salary.pop(salary.index(max(salary)))
        return sum(salary)/len(salary)