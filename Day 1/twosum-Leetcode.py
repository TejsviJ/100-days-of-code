class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(0,len(nums)):
            m=target-nums[i]
            dict[m]=i
           
        for i in nums:
            
            if i in dict:
                if (nums.index(i)!=dict.get(i)):
                    return ([nums.index(i),dict.get(i)])
