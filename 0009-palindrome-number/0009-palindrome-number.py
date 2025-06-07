class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Quick reject for negatives and any number ending in zero (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        original = x
        reversed_num = 0

        # Build the full reversed integer
        while x:
            reversed_num = reversed_num * 10 + (x % 10)
            x //= 10

        return reversed_num == original
