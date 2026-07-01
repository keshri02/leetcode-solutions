class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=""
        for ch in s:
            if ch.isalnum():
                result=result+ch.lower()
       # s=s.lower().replace(" ","")
        t=result[::-1]
        if t == result:
            return True
        else:
            return False


        