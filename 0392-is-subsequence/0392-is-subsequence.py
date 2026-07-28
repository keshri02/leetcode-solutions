class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        m=len(t)
        n=len(s)
        for i in range(m):
            if j<n and s[j]==t[i]:
                j+=1
        if j==n:
            return True
        else:
            return False


        