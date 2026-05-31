class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1

        for i in t:
            if i not in freq:
                return False
            freq[i]-=1
            if freq[i]==0:
                del freq[i]

        return len(freq)==0