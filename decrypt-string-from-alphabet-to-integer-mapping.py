class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        sol=""
        i=0
        while i<len(s):
            if i+2<len(s) and s[i+2]=="#":
                sol+=chr(int(s[i:i+2])+96)
                i+=2
            else:
                sol+=chr(int(s[i])+96)
            i+=1

        return sol
