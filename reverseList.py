'''1st solution'''
def reverseList_1(ls: list, acc, head=None) -> list:
  if len(ls) == 0:
    if head: 
      acc.append(head) 
    return acc
  
  reverseList_1(ls[1:], acc, ls[0])
  if head != None:
    acc.append(head)
  return acc

print(reverseList_1([4, 3, 2, 1], []))
print(reverseList_1([], []))


'''2nd solution'''
def reverseList_2(ls: list) -> list:
  if not ls:
    return []
  else:
    return reverseList_2(ls[1:]) + [ls[0]]

print(reverseList_2([4, 3, 2, 1]))
print(reverseList_2([]))