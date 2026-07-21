class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=len(accounts)
        n=len(accounts[0])
        temp=[]
        for i in range(m):
            add=0
            for j in range(n):
                add=add+accounts[i][j]
            temp.append(add)
        return max(temp)


        