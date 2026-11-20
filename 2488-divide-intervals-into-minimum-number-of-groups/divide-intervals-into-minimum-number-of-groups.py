class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        events = []

        for s, e in intervals:
            events.append((s, 1))
            events.append((e + 1, -1))

        events.sort()

        count = 0
        maxi = 0

        for time, value in events:
            count += value
            maxi = max(maxi, count)

        return maxi