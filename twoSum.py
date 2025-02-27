'''
nums = [2,7,11,15]
target = 9
output: [0,1]
'''

def twoSum(arr, target) -> list:
   
   ls = []
   if arr:
       for num in arr:
           i = target - num
           if i in ls:
               return [ls.index(i), arr.index(num)]
           ls.append(num)
   return


nums = [2,7,11,15]
target = 26
print(twoSum(nums, target))