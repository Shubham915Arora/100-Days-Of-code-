class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums=0
        pro=1
        while (n>0):
            x=n%10
            n=n//10
            sums=sums+x
            pro=pro*x
            
        return pro-sums
            