def find(dic, p):
    while dic[p] != p:
        p = find(dic, dic[p])
    return p

def union(dic, p1, p2):
    p1, p2 = find(dic, p1), find(dic, p2)
    dic[p1] = dic[p2] = min(p1, p2)

def connected(dic, p1, p2):
    return find(dic, p1) == find(dic, p2)

class Solution(object):  # Kruskal's algorithm O(E log V)
    def minCostConnectPoints(self, points):
        points = [tuple(p) for p in points]
        edges = []

        for i in xrange(len(points) - 1):
            for j in xrange(i + 1, (len(points))):
                dist = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
                edges.append((dist, points[i], points[j]))

        edges.sort(key=lambda edge: edge[0])

        min_cost = 0
        dic = {p: p for p in points}

        for edge in edges:
            (dist, p1, p2) = edge

            if not connected(dic, p1, p2):
                # print "here", edge
                union(dic, p1, p2)
                min_cost += dist

        return min_cost

print Solution().minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]])
print Solution().minCostConnectPoints(points = [[3,12],[-2,5],[-4,1]])
print Solution().minCostConnectPoints(points = [[0,0],[1,1],[1,0],[-1,1]])
print Solution().minCostConnectPoints(points = [[-1000000,-1000000],[1000000,1000000]])
print Solution().minCostConnectPoints(points = [[0,0]])
print Solution().minCostConnectPoints(points = [[2,-3],[-17,-8],[13,8],[-17,-15]])

