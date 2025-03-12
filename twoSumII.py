'''Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. 
Return the indices of the two numbers'''

def twoSum(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums)-1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left+1, right+1]
        elif current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
    return []