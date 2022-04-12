class Solution {
public:
    vector<vector<int>> result;
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> temp;
        solve(candidates,target,0,0,temp);
        
        return result;
    }
    
    void solve(vector<int>& candidates, int target, int sum, int index, vector<int>& temp){
        if(sum==target){
            result.push_back(temp);
            return;
        }
        
        if(sum>target || index>=candidates.size()){
            return;
        }
        
        
        for(int i=index;i<candidates.size();i++){
            temp.push_back(candidates[i]);
            solve(candidates,target,sum+candidates[i],i,temp);
            temp.pop_back();
        }
    }
};
