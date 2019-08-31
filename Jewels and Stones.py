class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        de={}
        sum=0
        for i in J:
            de[i]=0
            for j in S:
                if i == j:
                    de[i]+=1
                    sum+=1
        return sum
