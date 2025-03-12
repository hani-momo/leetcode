'''Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order.'''

def topKFrequent(nums: list[int], k: int) -> list[int]:
    bucket = [[] for i in range(len(nums) + 1)]
    frequencyMap = {}

    for n in nums:
        if n not in frequencyMap:
            frequencyMap[n] = 1
        else:
            frequencyMap[n] += 1

    for key, frequency in frequencyMap.items():
        bucket[frequency].append(key)

    res = []

    for i in reversed(range(len(bucket))):
        if bucket[i]:
            for value in bucket[i]:
                if len(res) < k:
                    res.append(value)
            else:
                return res
    
    return res