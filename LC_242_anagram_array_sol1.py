class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s) == sorted(t): #sort the strings into a sorted list and then compares the lists item by item
            return True
        else:
            return False