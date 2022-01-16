from collections import defaultdict
class Solution(object):  # Runtime: 180 ms, faster than 93.72%. Memory Usage: less than 97.51%
    def accountsMerge(self, accounts):
        def union(x, y):
            x, y = (find(x), find(y))
            if x == y: return 0
            if y < x: (x, y) = (y, x)
            parent[y] = x
            return 1

        def find(x):
            while x != parent[x]:
                x, parent[x] = parent[x], parent[parent[x]]
            return x

        node_to_name = {}
        email_to_node = {}
        parent = {}

        node_num = 0
        for li in accounts:
            node_to_name[node_num] = li[0]
            parent[node_num] = node_num

            for i in xrange(1, len(li)):
                email = li[i]

                if email in email_to_node:
                    union(node_num, email_to_node[email])
                else:
                    email_to_node[email] = node_num

            node_num += 1

        node_to_emails = defaultdict(list)
        for email in email_to_node:
            node_to_emails[find(email_to_node[email])].append(email)

        res = []
        for node in node_to_emails.keys():
            res.append([node_to_name[node]] + sorted(node_to_emails[node]))

        return res


print Solution().accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
print Solution().accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]])
