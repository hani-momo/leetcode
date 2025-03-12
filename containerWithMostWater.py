'''
Given an array of positive integers, 
each integer represents the height of a vertical line on a chart. 
Find two lines which together with the x-axis forms a container that would hold the greatest amount of water.
Return the area of water it would hold.
'''

'''O(n)'''
def maxArea(height) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        length = right - left
        area = min(height[left], height[right]) * length
        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
