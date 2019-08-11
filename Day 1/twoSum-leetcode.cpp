#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ves;
        for (int i=0;i<(nums.size())-1;i++){
            for (int j=i+1; j<(nums.size());j++){
                if((nums[i]+nums[j])==target){
                    ves.push_back(i);
                    ves.push_back(j);
                    
                    return ves;
                    
                }
              
            }
        }
        

    return ves;
} 
};
