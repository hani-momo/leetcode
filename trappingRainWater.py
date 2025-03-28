'''
Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it can trap after raining.
'''

def trappedWater(height: list[int]) -> int:

   left = 0
   right = len(height) - 1
   left_max = height[left]
   right_max = height[right]
   water = 0

   while left < right:
       if left_max < right_max:
           left += 1
           left_max = max(left_max, height[left])
           water += left_max - height[left]
       else:
           right -= 1
           right_max = max(right_max, height[right])
           water += right_max - height[right]
  
   return water


print(trappedWater([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trappedWater([0]))
