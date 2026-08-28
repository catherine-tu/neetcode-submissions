class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # add interval to list & sort by start
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        out = []

        # combine int if cur int start <= start <= cur int end
        smallest, largest = intervals[0]
        for start, end in intervals[1:]:
            # overlapping interval
            if (smallest <= start and start <= largest):
                smallest = min(smallest, start)
                largest = max(largest, end)
            # non-overlapping
            else:
                out.append([smallest, largest])
                smallest, largest = start, end
        
        out.append([smallest, largest])
        return out



        