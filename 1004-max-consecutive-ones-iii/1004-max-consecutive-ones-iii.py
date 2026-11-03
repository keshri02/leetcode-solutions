class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left=0
        countZero=0
        max_Length=0
        for right in range(len(nums)):
            if nums[right]==0:
                countZero+=1
            while countZero>k:
                if nums[left]==0:
                    countZero-=1
                left+=1
            max_Length=max(max_Length,right-left+1)
        return max_Length
    
            
        