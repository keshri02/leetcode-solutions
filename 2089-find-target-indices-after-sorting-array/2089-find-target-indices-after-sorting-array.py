class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort(); n=len(nums); temp=[]
        for i in range(n):
            if nums[i] == target:
                temp.append(i)
        return temp
        