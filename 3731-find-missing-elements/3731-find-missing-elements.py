class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()

        temp=[]
        result=[]

        j=nums[0]
        k=nums[-1]

        while j<=k:
            temp.append(j)
            j+=1
        
        i=0
        j=0

        while i<len(temp) and j<len(nums):
            if temp[i]==nums[j]:
                i+=1
                j+=1
            else:
                result.append(temp[i])
                i+=1
        
        return result