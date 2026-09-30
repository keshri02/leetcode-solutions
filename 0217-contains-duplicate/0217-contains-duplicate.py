class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        temp=nums
        nums1=set(nums)
        if len(nums1)==len(temp):
            return False
        else:
            return True

        