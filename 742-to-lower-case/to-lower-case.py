class Solution:
    def toLowerCase(self, s: str) -> str:
        new=""
        for i in s:
            asc=ord(i)
            if 65 <= asc <= 90:
                low=asc+32
                new+=chr(low)
            else:
                new+=chr(asc)
        return new 