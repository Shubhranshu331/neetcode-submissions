class Solution:
    def minWindow(self, s: str, t: str) -> str:
    
        if not s or not t or len(s) < len(t):
            return ""
        dict_t = Counter(t)
        required = len(dict_t)
        window_counts = {}
        formed = 0
        ans = float("inf"), None, None
        left = 0
        for right in range(len(s)):
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            while left <= right and formed == required:
                character = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                left += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]