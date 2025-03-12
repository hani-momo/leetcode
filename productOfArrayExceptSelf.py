'''Given an integer array nums, 
return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].'''

def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)

    left = [1] * n
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    right = [1] * n
    for i in range(n - 2, -1, -1):
        right *= right[i + 1] * nums[i + 1]
    
    result = [1] * n
    for i in range(n):
        result[i] = left[i] * right[i]

    return 