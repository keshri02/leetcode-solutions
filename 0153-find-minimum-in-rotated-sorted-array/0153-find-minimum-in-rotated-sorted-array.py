class Solution:
    def findMin(self, nums: List[int]) -> int:
       # nums.sort()
       #return nums[0]
       n=len(nums)
       left=0
       right=n-1
       while left<=right:
        mid=left+(right-left)//2
        if nums[mid]>nums[right]:
            left=mid+1
        elif nums[mid]<nums[right]:
            right=mid
        else:
            return nums[left]        