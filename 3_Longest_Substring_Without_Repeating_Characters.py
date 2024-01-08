#Accepted: 58ms, 17.41 MB
'''Given a string s, find the length of the longest substring without repeating characters.'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        lenght = 0

        for char in s:
            aux = substring.find(char)
            if aux == -1:
                substring = substring + char
            else:
                if len(substring) > lenght:
                    lenght = len(substring)
                substring = substring[aux + 1:] + char

        if len(substring) > lenght:
            lenght = len(substring)
        return lenght