class Solution {
public:
    int minOperations(vector<int>& nums, int x) 
    {
        int n=nums.size();
        int total=0;
        for (int num:nums)
        {
            total=total+num;
        }
        int target=total-x;
        if(target==0)
        return n;
        int left = 0;
        int sum = 0;
        int longest = -1;

        for (int right = 0; right < n; right++) {

            sum += nums[right];

            while (sum > target && left <= right) {
                sum -= nums[left];
                left++;
            }

            if (sum == target) {
                longest = max(longest, right - left + 1);
            }
        }

        if (longest == -1) {
            return -1;
        }

        return n - longest;
    }
};