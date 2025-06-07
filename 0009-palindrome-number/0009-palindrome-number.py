class Solution(object):
    def isPalindrome(self, x):
        """
        Determine whether an integer is a palindrome.

        Args:
            x (int): The integer to test.

        Returns:
            bool: True if x reads the same forward and backward, False otherwise.
        """
        # 1) Early exit: negative numbers can’t be palindromes
        #    because of the leading '-' sign.
        if x < 0:
            return False

        # 2) Convert to string so we can reverse it easily.
        s = str(x)

        # 3) Check equality with its reverse.
        #    s[::-1] returns the string from end → start.
        return s == s[::-1]
