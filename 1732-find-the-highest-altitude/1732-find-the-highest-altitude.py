class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude=[0]
        n=len(gain)
        for i in range(n):
            altitude.append(altitude[i]+gain[i])

        return(max(altitude))


