class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sorting the intervals based on the first key
        intervals.sort(key = lambda x: x[0])
        # Adding first interval
        output = [intervals[0]]
        # Merge remaining if
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            # if current start is less than prev end then 
            # its an overlap
            if start <= lastEnd:
                # sometimes cases like [1, 7], [2, 3]
                # hence taking the greatest end
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
        