class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        result=[0]*n
        k=0
        for num in nums:
            if num<pivot:
                result[k]=num
                k=k+1
        for num in nums:
            if num==pivot:
                result[k]=num
                k=k+1
        for num in nums:
            if num>pivot:
                result[k]=num
                k=k+1
        return result

        