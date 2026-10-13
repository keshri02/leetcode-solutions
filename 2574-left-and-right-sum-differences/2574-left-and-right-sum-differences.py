class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        left=0
        for i in range(n):
            ans[i]=left
            left=left+nums[i]
        right=0
        for i in range(n-1,-1,-1):
            ans[i]=abs(ans[i]-right)
            right=right+nums[i]
        return ans
        