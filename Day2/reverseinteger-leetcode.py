class Solution:
    def reverse(self, x: int) -> int:
        if(( x<(-2**31))or( x>(2**31)-1)):
            return 0;
        n=x
        if x<0:
            n*=-1;
        rev=0
        while(n>0):
            dig=n%10
            rev=rev*10+dig
            n=n//10
        if (x<0):
            rev*=-1
        if(( rev<(-2**31))or(rev>(2**31)-1)):
            return 0;
        
        return (rev);
        
