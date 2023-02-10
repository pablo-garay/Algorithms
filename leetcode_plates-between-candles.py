from bisect import *

class Solution(object):  # Runtime 1615 ms Beats 100%
    def platesBetweenCandles(self, s, queries):
        out = []
        candles = [i for i in xrange(len(s)) if s[i] == "|"]  # Time: O(n). Space: O(n) - in worst case. n=len(s)

        for (start, end) in queries:
            left, right = bisect_left(candles, start), bisect_right(candles, end) - 1  # O(log n) for each query in queries

            if left >= right:
                out.append(0)
            else:  # O(1)
                num_plates = (candles[right] - candles[left] - 1) - (right - left - 1)
                out.append(num_plates)
                # print (start, end), candles, left, right
        
        return out
