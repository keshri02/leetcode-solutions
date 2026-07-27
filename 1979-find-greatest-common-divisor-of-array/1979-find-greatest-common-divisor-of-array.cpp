class Solution {
public:
    int findGCD(vector<int>& nums) 
    {
        sort(nums.begin(),nums.end());
        int m=nums[0];
        int n=nums[nums.size()-1];
        while(n!=0)
        {
            int temp=n;
            n=m%n;
            m=temp;
        }
        return m;

    }
};