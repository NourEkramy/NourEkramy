from collections import defaultdict

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        cnt = Counter()
        for winner, loser in matches:
            if winner not in cnt:
                cnt[winner] = 0
            cnt[loser] += 1
        ans = [[], []]
        for i, occ in cnt.items():
            if occ < 2:
                ans[occ].append(i)
        ans[0].sort()
        ans[1].sort()
        return ans
