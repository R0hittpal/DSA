class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        end=float(-inf)
        count=0
        for current_start,current_end  in intervals:
            if current_start>=end:
                count+=1
                end =current_end
            
        return len(intervals)-count
        