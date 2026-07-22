class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret(2,0);
        map<int, int> vals; //val - > idx
        for(int i = 0; i < nums.size(); i++){
            vals[nums[i]] = i ;

        }

        for(int i = 0; i < nums.size(); i++){
            if(vals.find(target - nums[i]) != vals.end()){
                int j = vals[target-nums[i]];
                if(i != j){
                    ret[0] = i;
                    ret[1] = j;
                    return ret;
                }
            }
        }
        return ret;
    }
};
