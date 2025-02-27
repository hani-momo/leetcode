'''1st solution'''
def validParenthesis_1(s: str) -> bool:
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""

print(validParenthesis_1("()"))
print(validParenthesis_1("(]"))


'''2nd solution'''
def validParenthesis_2(s: str) -> bool:
   stack = []
   brackets = {")":"(", "}":"{", "]":"["}

   for char in s:
       if char in brackets:
           if not stack or stack[-1] != brackets[char]:
               return False
           stack.pop()
       else:
           stack.append(char)
  
   return len(stack) == 0

s = "()[]{}"
print(validParenthesis_2(s))
print(validParenthesis_2("(]"))
