class Solution(object):  # BFS solution: O(|nodes| + |edges|). Nodes: states, edges: possible actions
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        if targetCapacity > jug1Capacity + jug2Capacity:
            return False

        return self.bfs(jug1Capacity, jug2Capacity, targetCapacity)


    def bfs(self, jcap1, jcap2, targetCapacity):
        parent = {(0, 0): None}
        frontier = [(0, 0)]

        while frontier:
            next_frontier = []

            for (j1, j2) in frontier:
                if j1 + j2 == targetCapacity:
                    return True

                for state in [(jcap1, j2), (j1, jcap2), (0, j2), (j1, 0),
                              (0, j1 + j2) if j1 + j2 <= jcap2 else (j1 - (jcap2 - j2), jcap2),
                              (j1 + j2, 0) if j1 + j2 <= jcap1 else (jcap1, j2 - (jcap1 - j1))]:

                    if state not in parent:
                        next_frontier.append(state)
                        parent[state] = (j1, j2)

            frontier = next_frontier

        return False


print Solution().canMeasureWater(jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4)  # true
print Solution().canMeasureWater(jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5)  # false
print Solution().canMeasureWater(jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3)  # true
print Solution().canMeasureWater(jug1Capacity = 34, jug2Capacity = 5, targetCapacity = 6)  # true

