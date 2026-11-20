class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        start = sorted(x[0] for x in intervals)
        end = sorted(x[1] for x in intervals)

        count = 0
        j = 0

        for i in range(len(start)):
            if start[i] <= end[j]:
                count += 1
            else:
                j += 1

        return count