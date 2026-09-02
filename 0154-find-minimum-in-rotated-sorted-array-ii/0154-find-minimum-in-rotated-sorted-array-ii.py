class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        return nums[0]
        