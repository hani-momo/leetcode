'''Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.'''


def sortingApproach(nums: list[int]) -> bool:
    # O(nlogn)
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False


def hashsetApproach(nums: list[int]) -> bool:
    # O(n)
    seen = set() # sc = O(n)
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False