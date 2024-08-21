class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)

        x_rev = x_str[::-1]

        if x_str == x_rev:
            return True
        else:
            return False
