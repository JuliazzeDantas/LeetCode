#Accepted 50ms, 16.60MB
'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length=len(s)
        if length == 1:
            return s
        if numRows == 1:
            return s
        count=0
        interval=(numRows*2) - 3
        result = ''
        for row in range(0, numRows):
            if(row==0):
                while count < length:
                    result=result+s[count]
                    count=count+interval+1
            elif (row==numRows-1):
                while count+row < length:
                    result=result+s[count+row]
                    count=count+interval+1
            else:
                while count+row < length:
                    result=result+s[count+row]
                    if count+interval+1-row < length:
                        result=result+s[count+interval+1-row]
                    count=count+interval+1
            count = 0
        return result