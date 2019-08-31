class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N=len(A)/2
        o=N+1
        sum=0
        k={}
        for i in A:
            if i not in k:
                k[i]=1
            else:
                k[i] +=1        
        for i in k:
            if k[i]>sum:
                sum = k[i]
                l=i
        return l
        
