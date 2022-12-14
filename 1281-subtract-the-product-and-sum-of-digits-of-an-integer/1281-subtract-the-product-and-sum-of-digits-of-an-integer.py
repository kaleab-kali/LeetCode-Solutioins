class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # return eval('*'.join(str(n))) - eval('+'.join(str(n)))
        my_prod = 1
        my_sum = 0
        
        while n:
            n, remainder = divmod(n, 10)
            my_prod *= remainder            
            my_sum += remainder
            
        return my_prod - my_sum