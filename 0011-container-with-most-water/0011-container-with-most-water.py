class Solution:
    def maxArea(self, height: list[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        maxi=0
        while left<right:
            length=right-left
            h=min(height[left],height[right])
            water=length*h
            maxi=max(maxi,water)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxi
        