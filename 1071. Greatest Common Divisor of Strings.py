from fractions import gcd


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # if the concatenation of str1 and str2 is equal to the concatenation of str2 and str1
        if (str1 + str2) == (str2 + str1):

            # return the substring of str1 from 0 to the gcd of the length of str1 and str2
            length = gcd(len(str1), len(str2))

            # return the substring of str1 from 0 to the gcd of the length of str1 and str2
            return str1[:length]

        # if the concatenation of str1 and str2 is not equal to the concatenation of str2 and str1
        return ""
