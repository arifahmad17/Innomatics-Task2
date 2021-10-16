# Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum1=0
        p=1
        n=str(n)
        for i in range(len(n)):
            sum1=sum1+int((n[i]))
            p=p*int((n[i]))
        return (p-sum1)     
