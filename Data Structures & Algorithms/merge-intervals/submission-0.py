class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # track left & right, have conditions when to merge & when to start new

        # sort intervals by first
        intervals.sort() 

        l, r = intervals[0][0], intervals[0][1]
        out = []
        
        
        for inter in intervals:
            nl, nr = inter
            # new interval: new left > old right or new right < old left
            if nl > r or nr < l:
                out.append([l, r])
                l, r = nl, nr
            
            # expand int: nl or nr within old interval or new int surrounds
            if l <= nl <= r or l <= nr <= r or (nl < l and nr > r):
                l = min(l, nl)
                r = max(r, nr)
        
        # stragglers
        if l != intervals[0][0] or r != intervals[0][1] or len(out) == 0:
            print(l, r)
            out.append([l, r])
        
        return out
            




        # # first, sort intervals by start
        # srt_int = sorted(intervals, key=lambda x: x[0])
        # # print(intervals)
        # l, r = 0, 1

        # start, end = srt_int[0][0], srt_int[0][1]
        # out = []

        # # two pointer & track begin & end of intervals
        # while r < len(srt_int):
        #     # beginnings are already sorted. we care about the ends
        #     # check current end's with right's start -- if so, expand to bigger range
        #     if end >= srt_int[r][0]:
        #         end = max(end, srt_int[r][1])
        #     # otherwise, save int and continue
        #     else:
        #         out.append([start, end])
        #         start = srt_int[r][0]
        #         end = srt_int[r][1]

        #     # incr indexes no matter what
        #     l += 1
        #     r += 1
        
        # # lingering elts
        # out.append([start, end])
        
        return out
