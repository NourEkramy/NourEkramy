class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        x = ""
        if len(word1) >= len(word2):
            z = len(word1) - len(word2)
            word2 += '.' * z

            for i in range(len(word1)):
                x += word1[i]
                if word2[i] != '.':
                    x += word2[i]
        if len(word1) < len(word2):
            z = len(word2) - len(word1)
            word1 += '.' * z

            for i in range(len(word2)):
                if word1[i] != '.':
                    x += word1[i]
                x += word2[i]

        return x
