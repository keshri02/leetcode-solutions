class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*n
        sum=0
        for i in range(n):
            ans[i]=sum+nums[i]
            sum=sum+nums[i]
        return ans
        