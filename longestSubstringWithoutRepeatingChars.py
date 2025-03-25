'''given a string, 
find the length of the longest substring without repeating characters'''
import unittest

def longest_substring_without_repeating_chars(s: str) -> int:
    if not s:
        return 0
    
    start, end, max_length = 0, 0, 0
    char_set = set()
    
    while end < len(s):
        if s[end] not in char_set:
            char_set.add(s[end])
            max_length = max(max_length, end - start + 1)
            end += 1
        else:
            char_set.remove(s[start])
            start += 1
    
    return max_length


class test_longest_substring_without_repeating_chars(unittest.TestCase):
    def test_string_with_all_repeating_characters(self):
        s = "aaaaaa"
        self.assertEqual(longest_substring_without_repeating_chars(s), 1)

if __name__ == '__main__':
    unittest.main()