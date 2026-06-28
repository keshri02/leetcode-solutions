class Solution {
public:
    int maxProduct(vector<int>& nums) 
    {
        int n=nums.size();
        int maxProd=nums[0];
        for(int i=0;i<n;i++)
        {
            int mul=1;
            for(int j=i;j<n;j++)
            {
                mul=mul*nums[j];
                maxProd=max(maxProd,mul);
            }
           // maxProd=max(maxProd,mul);
        }
        return maxProd;
    }
};