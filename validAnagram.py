'''
Given two strings s and t return True if t is an anagram of s, and False otherwise
'''

def isAnagram(str1: str, str2: str) -> bool:
    str1 = str1.lower()
    str2 = str2.lower()

    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    counts = [0] * 26

    for char in str1:
        counts[ord(char) - ord('a')] += 1
    for char in str2:
        counts[ord(char) - ord('a')] -= 1

    for count in counts:
        if count !=0:
            return False
    
    return True
