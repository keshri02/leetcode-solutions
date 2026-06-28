class Solution {
public:
    int maxSubArray(vector<int>& nums) 
    {
        int n = nums.size();
        int res=nums[0];
        int maxSum=nums[0];
        for(int i = 1;i<n;i++)
        {
            maxSum=max(nums[i],maxSum+nums[i]);
            res=max(maxSum,res);
        }
        return res;
    }
};