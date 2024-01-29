# Accept: 26ms, 16.70MB
class Solution:
    def myAtoi(self, s: str) -> int:
        leng=len(s)
        count=0
        while (count<leng)and(s[count]==' '):
            count+=1
        if count==leng:
            return 0
        leng-=count
        s=s[count:]
        count=0
        max_num=2**31-1
        min_num=-(2**31)
        print(s)
        if leng==0:
            return 0
        if s[0]=='-':
            count+=1
            while (count<leng)and(s[count].isnumeric()):
                count+=1
            result=s[1:count]
            if ''==result:
                return 0
            else:
                result=(-1)*int(result)
                if(result<min_num):
                    return min_num
                else:
                    return result
        elif s[0]=="+":
            count+=1
            while (count<leng)and(s[count].isnumeric()):
                count+=1
            result=s[1:count]
            if ''==result:
                return 0
            else:
                result=int(result)
                if(result>max_num):
                    return max_num
                else:
                    return result
        else:
            while (count<leng)and(s[count].isnumeric()):
                count+=1
            result=s[0:count]
            if ''==result:
                return 0
            else:
                result=int(result)
                if(result>max_num):
                    return max_num
                else:
                    return result
        
