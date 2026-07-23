class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        combination1=str1+str2
        combination2=str2+str1
        if combination1 != combination2:
            return ""
        Divisor=gcd(len(str1),len(str2))
        return str1[0:Divisor] 
        