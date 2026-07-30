class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        temp=[0]*n
        j=0
        for i in range(n):
            if nums[i]%2==0:
                temp[j]=nums[i]
                j=j+1
        for i in range(n):
            if nums[i]%2!=0:
                temp[j]=nums[i]
                j=j+1
        return temp


        