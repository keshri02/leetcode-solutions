class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n= len(operations)
        result=[]
        """
        for i in range (n):
            if operations[i] == "C":
                result.pop()
            elif operations[i]=="D":
                result.append(result[-1]*2)
            elif operations[i] =="+":
                k=len(result)
                result.append(result[k-1]+result[k-2])
            else:
                result.append(int(operations[i]))
        """
        for char in operations:
            if char == "C":
                result.pop()
            elif char =="D":
                result.append(result[-1]*2)
            elif char =="+":
                k=len(result)
                result.append(result[k-1]+result[k-2])
            else:
                result.append(int(char))
        sum=0
        k=len(result)
        for i in range(k):
            sum=sum+result[i]
        return sum

        