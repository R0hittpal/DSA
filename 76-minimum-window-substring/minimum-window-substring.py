class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        hash_map = {}

        for ch in t:
            hash_map[ch] = hash_map.get(ch, 0) + 1

        left = 0
        cnt = 0
        minLen = float('inf')
        start = 0

        for right in range(len(s)):

            if s[right] in hash_map:
                hash_map[s[right]] -= 1

                if hash_map[s[right]] >= 0:
                    cnt += 1

            while cnt == len(t):

                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    start = left

                if s[left] in hash_map:
                    hash_map[s[left]] += 1

                    if hash_map[s[left]] > 0:
                        cnt -= 1

                left += 1

        if minLen == float('inf'):
            return ""

        return s[start:start + minLen]