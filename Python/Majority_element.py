'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''


from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        x = Counter(nums)
        x_values = list(x.values())
        x_keys = list(x.keys())
        max_count = max(x_values)
        max_number = x_keys [x_values.index(max_count)]

        return max_number
    
    
'''
Runtime
165 ms
Beats
80.62%

Memory
17.88 MB
Beats
98.83%
'''