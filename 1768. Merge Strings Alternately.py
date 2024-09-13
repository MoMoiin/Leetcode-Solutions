class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        # initialize the result string
        res = ""

        # iterate through the two strings using zip,
        # zip is used to iterate through two lists at the same time in python
        for l1, l2 in zip(word1, word2):
            res += l1 + l2

        # if the length of word1 is greater than word2, add the remaining characters of word1 to the result string
        diff = len(word1) - len(word2)

        # if the length of word2 is greater than word1, add the remaining characters of word2 to the result string
        if diff > 0:
            res += word1[-diff:]

        # if the length of word1 is greater than word2, add the remaining characters of word1 to the result string
        elif diff < 0:
            res += word2[diff:]

        # if the length of word1 is equal to word2, return the result string
        return res
