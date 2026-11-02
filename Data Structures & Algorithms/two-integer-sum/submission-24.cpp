class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> target_indices;
        unordered_map<int,int> hash_table;

        for(int i = 0; i < nums.size(); i++){
            int key = target - nums[i];
            

            if(hash_table.find(key) != hash_table.end()){
                return {hash_table[key], i};
            } else{
                hash_table[nums[i]] = i;
            }
            
        }
    }
};
