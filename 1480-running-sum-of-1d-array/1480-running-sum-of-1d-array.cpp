class Solution {
public:
    vector<int> runningSum(vector<int>& nums) 
    {
        int n=nums.size();
        vector<int>result(n,0);
        int left=0;
        for(int i =0;i<n;i++)
        {
            left=left+nums[i];
            result[i]=left;
        }
        return result;
    }
};