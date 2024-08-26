class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> v;
       
        vector<int> ret;
        for (int i = 0; i < nums.size(); i++) {
            if (v.find(target - nums[i]) != v.end() && v.find(target - nums[i])->second != i) {
                auto it = v.find(target - nums[i]);
                ret.push_back(i);
                ret.push_back(it->second);
                break;
            }
            v.insert({nums[i], i});
        }
        return ret;
    }
};