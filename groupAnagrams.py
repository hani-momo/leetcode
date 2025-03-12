'''Given an array of strings strs, group the anagrams together. 
You can return the answer in any order
'''
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    if not strs:
        return []
    
    anagrams = {} # frequency of letters in string: [strings with the same frequency]

    def get_frequency_string(element) -> str:
        freq_list = [0] * 26

        for char in element:
            freq_list[ord(char) - ord('a')] += 1

        frequency_string = []
        char = 'a'
        for position in freq_list:
            frequency_string.append(char)
            frequency_string.append(str(position))
            char = chr(ord(char) + 1)

        return ''.join(frequency_string)
    
    for element in strs:
        frequency_string = get_frequency_string(element)

        if frequency_string not in anagrams:
            anagrams[frequency_string] = []
        
        anagrams[frequency_string].append(element)

    return list(anagrams.values())


'''2nd solution'''
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups = {}

    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagram_groups:
            anagram_groups[sorted_s] = []
        anagram_groups[sorted_s].append(s)

    return list(anagram_groups.values())