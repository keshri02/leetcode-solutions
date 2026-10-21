class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        total_sum=sum(nums)
        left_sum=0
        for i in range(1,n):
            left_sum+=nums[i-1]
            right_sum=total_sum-left_sum
            diff=abs(right_sum-left_sum)
            if diff%2==0:
                count+=1
        return count
        