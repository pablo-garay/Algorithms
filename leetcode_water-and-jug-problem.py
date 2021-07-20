class Solution(object):
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        if targetCapacity > jug1Capacity + jug2Capacity:
            return False

        return self.bfs(jug1Capacity, jug2Capacity, targetCapacity)


    def bfs(self, jcap1, jcap2, targetCapacity):
        parent = {(0, 0): None}
        level = {}
        frontier = [(0, 0)]
        curr_level = 1

        while frontier:
            next_frontier = []

            for (j1, j2) in frontier:
                if j1 + j2 == targetCapacity:
                    return True

                if j1 < jcap1 and (jcap1, j2) not in parent:
                    next_frontier.append((jcap1, j2))
                    parent[(jcap1, j2)] = (j1, j2)

                if j2 < jcap2 and (j1, jcap2) not in parent:
                    next_frontier.append((j1, jcap2))
                    parent[(j1, jcap2)] = (j1, j2)

                if (0, j2) not in parent:
                    next_frontier.append((0, j2))
                    parent[(0, j2)] = (j1, j2)

                if (j1, 0) not in parent:
                    next_frontier.append((j1, 0))
                    parent[(j1, 0)] = (j1, j2)

                if j2 < jcap2 and j1 > 0:
                    if j2 + j1 <= jcap2:
                        if (0, j1 + j2) not in parent:
                            next_frontier.append((0, j1 + j2))
                            parent[(0, j1 + j2)] = (j1, j2)
                    else:
                        diff = jcap2 - j2
                        if (j1 - diff, jcap2) not in parent:
                            next_frontier.append((j1 - diff, jcap2))
                            parent[(j1 - diff, jcap2)] = (j1, j2)

                if j1 < jcap1 and j2 > 0:
                    if j1 + j2 <= jcap1:
                        if (j1 + j2, 0) not in parent:
                            next_frontier.append((j1 + j2, 0))
                            parent[(j1 + j2, 0)] = (j1, j2)
                    else:
                        diff = jcap1 - j1
                        if (jcap1, j2 - diff) not in parent:
                            next_frontier.append((jcap1, j2 - diff))
                            parent[(jcap1, j2 - diff)] = (j1, j2)

            frontier = next_frontier

        return False


print Solution().canMeasureWater(jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4)  # true
print Solution().canMeasureWater(jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5)  # false
print Solution().canMeasureWater(jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3)  # true
print Solution().canMeasureWater(jug1Capacity = 34, jug2Capacity = 5, targetCapacity = 6)  # true

