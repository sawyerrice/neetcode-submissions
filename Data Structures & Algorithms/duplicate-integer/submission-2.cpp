class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        map<int,int> vals;
        for(int i = 0; i < nums.size(); i++){

            if(vals.find(nums[i]) == vals.end() ){
                vals[nums[i]] = 1;
            }else{
                return true;
            }
        }
        return false;


    }
};
