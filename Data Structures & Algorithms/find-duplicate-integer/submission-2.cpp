class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        map<int, int> vals;

        for(int i =0; i < nums.size(); i++){
            if(vals.find(nums[i]) != vals.end()){
                return nums[i];
            }else{
                vals[nums[i]] = 1;
            }
        }

        return -1;
    }
};
