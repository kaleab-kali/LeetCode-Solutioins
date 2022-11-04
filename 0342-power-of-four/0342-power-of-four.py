class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        bin_num = bin(n)
        zero_count = bin_num.count('0')
        return zero_count % 2 == 1 and bin_num[2] == '1' and zero_count + 2 == len(bin_num)