class Solution {
public:
    bool isPalindrome(int x) 
    {
        int d;
        long int rev=0;
        int temp=x;
        if (temp<0)
        return false;
        while(temp!=0)
        {
            d=temp%10;
            rev=rev*10+d;
            temp=temp/10;
        }
        if(rev==x)
        return true;
        return false;
        
    }
};