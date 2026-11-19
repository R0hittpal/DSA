class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []
        last = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= last[1]:
                last[1] = max(last[1], intervals[i][1])
            else:
                ans.append(last)
                last = intervals[i]

        ans.append(last)
        return ans