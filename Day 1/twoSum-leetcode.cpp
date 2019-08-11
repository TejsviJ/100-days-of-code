#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ves;
        for (int i=0;i<sizeof(nums);i++){
            for (int j=i; j<sizeof(nums);j++){
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
