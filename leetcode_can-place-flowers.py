class Solution(object):  # Time: O(m) where m is length of array - optimal as need to traverse whole array in worst case. Space: O(1)
    def canPlaceFlowers(self, flowerbed, n):  # GREEDY algorithm. # Runtime: 124 ms, faster than 98.55%  # Memory Usage: less than 85.82%
        i = 0; options = 0

        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i - 1 < 0 or flowerbed[i - 1] == 0) and (i + 1 >= len(flowerbed) or flowerbed[i + 1] == 0):
                options += 1
                i += 2
                continue
            i += 1

        return options >= n