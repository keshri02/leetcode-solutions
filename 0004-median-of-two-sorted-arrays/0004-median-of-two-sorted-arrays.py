class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=len(nums1)
        n2=len(nums2)
        merge=[0]*(n1+n2)
        i=j=k=0
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                merge[k]=nums1[i]
                k=k+1
                i=i+1
            else:
                merge[k]=nums2[j]
                k=k+1
                j=j+1
        while i<n1:
            merge[k]=nums1[i]
            k=k+1
            i=i+1
        while j<n2:
            merge[k]=nums2[j]
            k=k+1
            j=j+1
        m=len(merge)
        if m %2!=0:
            low=0
            high=m-1
            mid=(low+high)//2
            return merge[mid]
        else:
            return (merge[(m//2)-1]+merge[m//2])/2

        
        