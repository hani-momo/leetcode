'''Given an integer array nums and an int k. 
find a contiguous subarray whose length is equal to k 
that has the largest average value and return this value'''
import unittest


def findMaxAverage(nums: list[int], k: int) -> float: # O(n) time, O(1) space
    if not nums:
        raise ValueError("nums cannot be empty")
    
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]

    max_sum = current_sum

    start_index = 0
    end_index = k

    while end_index < len(nums):
        current_sum -= nums[start_index]
        start_index += 1

        current_sum += nums[end_index]
        end_index += 1

        max_sum = max(max_sum, current_sum)

    return max_sum / k


class TestFindMaxAverage(unittest.TestCase):
    def test_k_is_1(self):
        nums = [1, 2, 3, 4, 5]
        k = 1
        self.assertEqual(findMaxAverage(nums, k), 5.0)

    def test_k_equals_len_nums(self):
        nums = [1, 2, 3, 4, 5]
        k = len(nums)
        self.assertEqual(findMaxAverage(nums, k), 3.0)
    
    def test_empty_array(self):
        nums = []
        k = 3
        with self.assertRaises(ValueError):
            findMaxAverage(nums, k)


if __name__ == '__main__':
    unittest.main()