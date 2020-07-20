class Solution:
    def isPalindrome(self, x: int) -> bool:
        c=x
        n=0
        while(x>0):
            a=x%10
            x=x//10
            n=(n*10)+a
        
    
        
        if n==c:
            return True
        
        else : 
            return False
        