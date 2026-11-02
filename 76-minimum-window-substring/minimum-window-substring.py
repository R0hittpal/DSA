class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if m > n:
            return ""

        hash_map = [0] * 256

        for ch in t:
            hash_map[ord(ch)] += 1

        left = 0
        right = 0
        cnt = 0

        minLen = float('inf')
        sIndex = -1

        while right < n:

            # Expand window
            if hash_map[ord(s[right])] > 0:
                cnt += 1

            hash_map[ord(s[right])] -= 1

            # Shrink window
            while cnt == m:

                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    sIndex = left

                hash_map[ord(s[left])] += 1

                if hash_map[ord(s[left])] > 0:
                    cnt -= 1

                left += 1

            right += 1

        if sIndex == -1:
            return ""

        return s[sIndex:sIndex + minLen]