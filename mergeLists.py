
'''
left_ids = [1, 3, 5, 6, 8]
right_ids = [2, 3, 5, 8, 10]
res = [1, 2, 3, 4, 5, 5, 6 ...]
'''

def mergeSortedLists(first_ls: list, second_ls: list) -> list:
   merged_list = []
   first_idx, second_idx = 0, 0

   while first_idx < len(first_ls) and second_idx < len(second_ls):
       if first_ls[first_idx] < second_ls[second_idx]:
           merged_list.append[first_ls[first_idx]]
           first_idx += 1
       else:
           merged_list.append[second_ls[second_idx]]
           second_idx += 1
  
   while first_idx < len(first_ls):
       merged_list.append(first_ls[first_idx])
       first_idx += 1
   while second_idx < len(second_ls):
       merged_list.append(second_ls[second_idx])
       second_idx += 1

   return merged_list


left_ids = [1, 3, 5, 6, 8]
right_ids = [2, 3, 5, 8, 10]
longer_ids = [2, 3, 5, 8, 10, 12, 15]
print(mergeSortedLists(left_ids, right_ids))
print(mergeSortedLists(left_ids, longer_ids))
