class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = {}
        for i in range(len(s)):
            set1[s[i]] = set1.get(s[i],0)+1
        for j in range(len(t)):
            if t[j] not in set1:
                return False
            elif t[j] in set1 and set1[t[j]] == 0:
                return False
            else:
                set1[t[j]] -= 1
        return True
s = Solution()
print(s.isAnagram(s = "ab", t = "ba"))