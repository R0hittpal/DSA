class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        n = len(s)
        sign = 1
        num = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Step 1: Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Step 2: Check sign
        if i < n and s[i] == "-":
            sign = -1
            i += 1

        elif i < n and s[i] == "+":
            i += 1

        # Step 3: Convert digits
        while i < n and s[i].isdigit():

            digit = int(s[i])

            num = num * 10 + digit

            # Step 4: Check overflow
            if sign * num > INT_MAX:
                return INT_MAX

            if sign * num < INT_MIN:
                return INT_MIN

            i += 1

        return sign * num