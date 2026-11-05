class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        left = 0
        dictt = {}
        count = 0

        for right in range(n):
            ch = s[right]
            dictt[ch] = dictt.get(ch, 0) + 1

            while dictt.get('a', 0) > 0 and dictt.get('b', 0) > 0 and dictt.get('c', 0) > 0:
                count += n - right

                dictt[s[left]] -= 1
                left += 1

        return count