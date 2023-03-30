class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set(nums)

        if len(nums) != len(hashset):
            return True
        return False