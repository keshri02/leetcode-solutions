class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums); total=0 ; i=1; sum=0
        while i<=n:
            total=total+i
            i+=1
        for i in range(n):
            sum=sum+nums[i]
        return total-sum
        