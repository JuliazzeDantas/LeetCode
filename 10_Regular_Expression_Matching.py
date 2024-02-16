p='.'
s='aa'
if True:
    if True:
        flag = False
        length_s=len(s)
        length_p=len(p)
        if (p=='.')and(length_s==1):
            print(True)
        if (p=='.*'):
            print(True)
        if p==s:
            print(True)
        count_s=count_p=0
        while (count_s<length_s)or(count_p<length_p):
            if (p[count_p] == '.')and(p[count_p+1] == '*'):

                
            elif (p[count_p] == '.') and ((count_p < length_p) or (p[count_p+1] != '*')) and (count_s < length_s):
                count_s+=1
                count_p+=1
                flag=True
        
        if flag==True:
            print("OK")
            


        



