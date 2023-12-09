class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, su = 1, 0
        m = n
        while m > 0:
            prod *= m%10
            su += m%10
            m = m//10
        return prod - su
