from collections import defaultdict  # Runtime: 424 ms, faster than 95.74%. Best we can do O(n^2) as output in worst case is nxn matrix
class Solution(object):  # Time: O(n log n + n^2) as need to sort to give output and in worst case each order introduces new table & new item at same time (so we might have n tables and n items)
    def displayTable(self, orders):  # Space: O(n^2) each order in worst case introduces new table & new item (n tables, n items)
        items = set()
        mapping = defaultdict(lambda: defaultdict(int))  # this is super cool, use it in the future wisely
        out = []

        for (_, table, item) in orders:
            mapping[int(table)][item] += 1
            items.add(item)
        # print mapping
        items = sorted(items)

        first_row = ["Table"]
        for item in items: first_row.append(item)
        out.append(first_row)

        for table in sorted(mapping.keys()):
            row = [str(table)]
            for item in items: row.append(str(mapping[table][item]))
            out.append(row)

        return out


print Solution().displayTable(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]])
print Solution().displayTable(orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]])
