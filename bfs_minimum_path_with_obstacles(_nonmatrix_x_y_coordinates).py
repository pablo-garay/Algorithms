class Solution():
    def solve(self, src_x, src_y, dest_x, dest_y, barriers):
        self.parent = {(src_x, src_y): None}; output = []
        self.bfs(src_x, src_y, dest_x, dest_y, barriers)
      
        child = (dest_x, dest_y) 
        while self.parent[child] is not None:
            (px, py, dir) = self.parent[child]
            # print (px, py), ">", dir, ">", child
            output.append(dir)
            child = (px, py)

        output.reverse()
        return " ".join(output)


    def bfs(self, x, y, dest_x, dest_y, barriers):
        frontier = [(x, y)]

        while frontier:
            next_frontier = []

            for (x1, y1) in frontier:
                for (x2, y2, dir) in [(x1 + 1, y1, "E"), (x1 - 1, y1, "W"), (x1, y1 + 1, "N"), (x1, y1 - 1, "S")]:
                    
                    if (x2, y2) not in self.parent and (x2, y2) not in barriers:
                        # print (x1, y1), "->", dir, "->", (x2, y2)
                        self.parent[(x2, y2)] = (x1, y1, dir)

                        if (x2, y2) == (dest_x, dest_y):
                            return (x2, y2)

                        next_frontier.append((x2, y2))

            frontier = next_frontier



print Solution().solve(src_x=1, src_y=1, dest_x=3, dest_y=4, barriers=[])
print Solution().solve(src_x=1, src_y=1, dest_x=3, dest_y=4, barriers={(1, 3), (3, 1), (3, 2), (3, 3)})


# 4     D
# 3 x   x  
# 2     x
# 1 C   x
# 0 1 2 3 4

# EENNN
# ENNNE
