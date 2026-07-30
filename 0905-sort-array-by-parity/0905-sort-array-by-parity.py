class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        temp=[0]*n
        left=0
        right=n-1
        for i in range(n):
            if nums[i]%2==0:
                temp[left]=nums[i]
                left=left+1
            else:
                temp[right]=nums[i]
                right=right-1
        return temp


        