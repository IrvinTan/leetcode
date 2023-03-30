class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i, value in enumerate(nums):
            other_num = target - nums[i]

            if other_num in seen:
                return [i, seen[other_num]]
            else:
                seen[value] = i