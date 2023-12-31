class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        oneto19 = ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine', ' Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen']
        tens = ['', ' Ten', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
        thousands = ['', ' Thousand', ' Million', ' Billion']
    

        def helper( n: int) -> str:
            if n < 20:
                return oneto19[n]
            elif n < 100:
                return tens[n // 10] + helper(n % 10)
            elif n < 1000:
                return helper(n // 100) + ' Hundred' + helper(n % 100)
            else:
                for i in range(3, 0, -1):
                    if n >= 1000 ** i:
                        return helper(n // (1000 ** i)) + thousands[i] + helper(n % (1000 ** i))
            return ''

        return helper(num).lstrip()
