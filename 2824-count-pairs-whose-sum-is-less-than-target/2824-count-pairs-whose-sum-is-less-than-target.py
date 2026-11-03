class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        left=0
        count=0
        n=len(nums)
        for left in range(n):
            for right in range(left+1,n):
                if nums[left] + nums[right] < target:
                    count+=1
        return count

        