class Solution {
public:
    int largestAltitude(vector<int>& gain) 
    {
        int n=gain.size();
        vector<int>altitude(n+1,0);
        int result=0;
        int j=0;
        for(int i=0;i<n;i++)
        {
            result=result+gain[i];
            altitude[j]=result;
            j++;
        }
        return *max_element(altitude.begin(),altitude.end());
    }
};