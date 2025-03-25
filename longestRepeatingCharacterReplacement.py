'''Given a string s and int k,
you can choose any character of the string 
and change it to any other character.
You can perform this operation at most k times.
Find the length of the longest substring containing the same character'''
import unittest

def character_replacement(s: str, k: int) -> int: # O(n) time, O(1) space
    count = {}

    start, max_length, max_repeat = 0, 0, 0

    for end in range(len(s)):
        count[s[end]] = count.get(s[end], 0) + 1

        max_repeat = max(max_repeat, count[s[end]])

        window = end - start + 1
        if (window - max_repeat) > k: # according to number ofallowed replacements
            count[s[start]] -= 1
            start += 1
        
        window = end - start + 1
        max_length = max(max_length, window)

    return max_length
    

class test_character_replacement(unittest.TestCase):
    def test_k_equals_0(self):
        s = "ABAB"
        k = 0
        self.assertEqual(character_replacement(s, k), 1)
    
    def test_k_equals_len_s(self):
        s = "ABABABB"
        k = len(s)
        self.assertEqual(character_replacement(s, k), len(s))
    
    def test_empty_string(self):
        s = ""
        k = 2
        self.assertEqual(character_replacement(s, k), 0)

if __name__ == '__main__':
    unittest.main()

