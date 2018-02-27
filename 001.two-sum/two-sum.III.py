"""
* Design and implement a TwoSum class. It should support the following operations: add and find.
* 
* add - Add the number to an internal data structure.
* find - Find if there exists any pair of numbers which sum is equal to the value.
* 
* For example,
*
*   add(1); add(3); add(5);
*   find(4) -> true
*   find(7) -> false
"""

class TwoSum(object):
    def __init__(self):
        nums = {}

    def add(num):
        self.nums[num] += 1

    def find(value):
        for first in self.nums.keys():
            second = value - first

            if second in self.nums && (first != second || (first == second && self.nums[first] > 1)):
                return True
        return False

