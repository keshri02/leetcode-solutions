class Solution {
public:
    long long countCommas(long long n) 
    {
        long long p=1000;
        long long count=0;
        if (n<1000)
        return 0;
    
        while(p<=n)
        {
            count=count+n-p+1;
            p=p*1000;
                
        }
        return count;
    }//use digit count concept using while loop with %100
};