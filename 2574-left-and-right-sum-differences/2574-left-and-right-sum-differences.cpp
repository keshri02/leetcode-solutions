class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) 
    {
        int n=nums.size();
        vector<int>result(n,0);
        int left=0;
        for(int i=0;i<n;i++)
        {
            result[i]=left;
            left=left+nums[i];
        }
        int right=0;
        for(int i=n-1;i>-1;i--)
        {
            result[i]=abs(result[i]-right);
            right=right+nums[i];
        }
        return result;
    }
};