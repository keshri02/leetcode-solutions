class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr=sorted(set(arr))
        n=len(sorted_arr)
        rank={}
        for i in range(n):
            rank[sorted_arr[i]]=i+1
        answer=[]
        for x in arr:
            answer.append(rank[x])
        return answer

