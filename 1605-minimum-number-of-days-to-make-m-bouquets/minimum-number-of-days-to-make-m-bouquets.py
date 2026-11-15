class Solution:
    def possible(self, arr, day, m, k):
        count = 0
        buq = 0

        for num in arr:
            if num <= day:
                count += 1
            else:
                buq += count // k
                count = 0

        buq += count // k

        return buq >= m

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if m * k > n:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if self.possible(bloomDay, mid, m, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans