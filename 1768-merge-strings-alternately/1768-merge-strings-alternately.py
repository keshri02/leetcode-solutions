class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)<=len(word2):
            n=len(word2)
        else:
            n=len(word1)
        result=""
        for i in range(n):
            if i< len(word1):
                result=result+word1[i]
            if i<len(word2):
                result=result+word2[i]
        return result
        