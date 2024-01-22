# Accepted 32ms, 16.52MB

class Solution:
    def reverse(self, x: int) -> int:
        result=0
        aux = 0
        if x>=0:
            while x!=0:
                result*=10
                aux=x%10
                x=(x-aux)//10
                result+=aux
            if result<pow(2,31):
                return result
            else:
                return 0
        else:
            while x!=0:
                result*=10
                aux=x%(-10)
                x=(x-aux)//10
                result+=aux
            if result>=pow(-2,31):
                return result
            else:
                return 0

