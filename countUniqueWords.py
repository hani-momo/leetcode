'''
Count unique words in the string. The input does not contain punctuation.
'''

def countUniqueWords(s: str) -> dict:
    cleaned_text = s.lower()
    words = cleaned_text.split()
    
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

s = "This is a test test"
print(countUniqueWords(s))