'''
Finds all anagrams of a given word. 
E.g. given the dictionary content: “aba”,  “baa”, “bab”;
will return Set(“aba”, “baa”) for a searchWord “aab”
'''

def anagram(ls: list, searchWord: str) -> set:
  result = set()
  sortedSearchWord = sorted(searchWord)
  
  for s in ls:
    if sorted(s) == sortedSearchWord:
      result.add(s)
  return result

search = "aab"
example = ["aba", "baa", "bab"]
print(anagram(example, search))