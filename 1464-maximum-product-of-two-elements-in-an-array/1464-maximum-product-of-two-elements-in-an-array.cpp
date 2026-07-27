class Solution {
public:
    int maxProduct(vector<int>& nums)
    {
        vector<int> temp;
        int result=0;
        temp=nums;
        sort(temp.begin(),temp.end());
        int n=temp.size();
        result=((temp[n-1]-1)*(temp[n-2]-1));
        return result;

    }
};