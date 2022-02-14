from collections import defaultdict
class Solution(object):  # Runtime: 424 ms, faster than 95.74%
    def displayTable(self, orders):  # Time: O(n log n) as need to sort to give output. Space: O()
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
