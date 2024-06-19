'''
https://leetcode.com/problems/insert-interval/description/
'''
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []

        for i in range(len(intervals)):
            # return so far added intervals along with newone and 
            # remaining without iterating
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # Adding all intervals comes before newinterval and without overlap
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # If overlap found
            else:
                # newinterval is modified and will continue iterate
                newInterval = [min(newInterval[0], intervals[i][0]), 
                               max(newInterval[1], intervals[i][1])]
                
        # if the new interval comes withing the intervals
        # the above loop return the result if interval is at last then
        res.append(newInterval)
        return res             
