class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        arr=[0,0]
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    arr[0]=i
                    arr[1]=j
                    #return arr
        return arr