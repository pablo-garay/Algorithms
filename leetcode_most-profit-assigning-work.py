class Solution(object):  # Runtime: 324 ms, faster than 90.57% . Memory Usage: less than 100.00%
    def maxProfitAssignment(self, difficulty, profit, worker):  # Time: O(m log m + n log n)
        map1 = [(profit[i], difficulty[i]) for i in xrange(len(profit))]  # O(n)
        map1.sort(reverse=True)  # O(n log n)

        map2 = [map1[0]]
        for i in xrange(1, len(map1)):  # O(n)
            if map1[i][1] < map2[-1][1]:
                map2.append(map1[i])

        worker.sort(reverse=True)  # O(m log m)

        tot_prof = 0
        i1, i2 = (0, 0)

        while i1 < len(worker) and i2 < len(map2):  # O(m + n)
            if worker[i1] >= map2[i2][1]:
                tot_prof += map2[i2][0]
                i1 += 1
            else:
                i2 += 1

        return tot_prof


print Solution().maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7])
print Solution().maxProfitAssignment(difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25])
print Solution().maxProfitAssignment(difficulty = [5,3,2,4,1], profit = [10,20,30,40,50], worker = [4,5,6,7])
