# Accepted 32ms, 16.52MB
'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.'''
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

