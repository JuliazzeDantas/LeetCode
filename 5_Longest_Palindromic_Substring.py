# Accept 58ms, 16.70MB
'''Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        length = len(s)
        if length==1:
            return s
        size=1
        start=0
        count=1
        big=small=result=s[0]
        while count<length:
            if s[start:count+1][::-1] in s[start:]:
                small=s[start:(2*count)-start]
                big=s[start:(2*count)-start+1]
                itself=s[start:count+1]
                if small==small[::-1]:
                    if len(small)>size:
                        size = len(small)
                        result = small
                if big==big[::-1]:
                    if len(big)>size:
                        size=len(big)
                        result=big
                if itself==itself[::-1]:
                    if size<len(itself):
                        result=itself
                count+=1
            else:
                if(count-start)==1:
                    count+=1
                start+=1
        return result