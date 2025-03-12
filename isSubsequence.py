'''Given two strings, return True if one string is a subsequence of the second'''

def isSubsequence(str1: str, str2: str) -> bool: # O(n)
    first = 0
    second = 0

    while first < len(str1) and second < len(str2):
        if str1[first] == str2[second]:
            first += 1
            second += 1
        else:
            second += 1

    return first == len(str1)