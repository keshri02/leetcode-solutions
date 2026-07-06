class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        low=0
        high=n-1
        maxi=0
        while low<high:
            lenght=high-low
            h=min(height[high],height[low])
            water=h*lenght
            maxi=max(maxi,water)
            if height[low]<height[high]:
                low=low+1
            else:
                high=high-1
        return maxi
        