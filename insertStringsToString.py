'''
Given an original string string and a dictionary elements, 
where the keys represent the indices for insertion 
and the values are the strings to be inserted at these indices.

input: 'hello', {1: '1', 4: '4'}
output: 'h1ell4o'

input: 'cat', {2: 'dog', 0: 'a'}
output: 'acadogt'
'''

def insertStrings(string: str, elements: dict) -> str:
   result = list(string)
   for idx in sorted(elements.keys(), reverse=True):
       result.insert(idx, elements[idx])

   return ''.join(result)


string = 'hello'
elements = {
   1: '1',
   4: '4'
}
print(insertStrings(string, elements))

string = 'cat'
elements = {
   2: 'dog',
   0: 'a'
}
print(insertStrings(string, elements))