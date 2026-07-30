class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        temp=[0]*n
        j=0
        for i in range(n):
            if j>=n:
                break
            temp[j]=arr[i]
            j=j+1
            if arr[i] ==0 and j<n:
                temp[j]=0
                j=j+1
        for i in range(n):
            arr[i]=temp[i]

        