from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        overlapping = lambda x, y: x[1] >= y[0]
        output = [intervals[0]]
        for span in intervals[1:]:
            if overlapping(output[-1], span):
                output[-1][1] = max(output[-1][1], span[1])
            else:
                output.append(span)
        return output