from heapq import *
class Solution(object):  # Runtime: 712 ms, faster than 90.91%
    def smallestChair(self, times, targetFriend):  # Time: O(n log n). Space: O(n) where n = len(times)
        chair_count = 0; freed = []; chair_assignm = {}
        events = []

        for (friend_num, (arrival, depart)) in enumerate(times):
            events.append((depart, 0, friend_num))   # 0 comes before 1 when sorting, so departures come first
            events.append((arrival, 1, friend_num))  # arrival after departure

        events.sort(key=lambda e: (e[0], e[1]))  # O(n log n)

        for (time, etype, friend_num) in events:  # O(n log n) total as traversing n elems and spending log n in worst case
            # print (time, etype, friend_num), freed, chair_count
            if etype == 1:  # arrival
                if freed:
                    num = heappop(freed)  # O(log n)
                else:
                    num = chair_count
                    chair_count += 1

                if targetFriend == friend_num: return num
                chair_assignm[friend_num] = num

            else:  # etype == 0 i.e. departure
                heappush(freed, chair_assignm[friend_num])  # O(log n)

        return None


print Solution().smallestChair(times = [[1,4],[2,3],[4,6]], targetFriend = 1)
print Solution().smallestChair(times = [[3,10],[1,5],[2,6]], targetFriend = 0)
