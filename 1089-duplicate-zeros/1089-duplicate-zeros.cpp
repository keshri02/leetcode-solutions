class Solution {
public:
    void duplicateZeros(vector<int>& arr) 
    {
        int n = arr.size();
        int j=0;
        vector<int>temp(n);
        for (int i=0;i<n && j<n;i++)
        {
            temp[j++]=arr[i];
            if (arr[i]==0 && j<n)
            {
                temp[j++]=0;
            }
        }
        arr =temp;
    }
};