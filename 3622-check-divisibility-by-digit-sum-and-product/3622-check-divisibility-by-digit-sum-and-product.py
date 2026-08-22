class Solution:
    def checkDivisibility(self, n: int) -> bool:
        Digit_sum=0
        Digit_prod=1
        temp=n
        while temp !=0:
            d=temp%10
            Digit_sum=Digit_sum+d
            Digit_prod=Digit_prod*d
            temp=temp//10
        if Digit_prod == 0: 
            return n % Digit_sum == 0
        if n % (Digit_sum + Digit_prod)==0:
            return True
        else:
            return False

        