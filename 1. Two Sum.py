class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_to_index = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in number_to_index:
                return [number_to_index[difference], i]
            number_to_index[num] = i
