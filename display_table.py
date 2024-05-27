from typing import List
from collections import Counter


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        tables = {}
        for o in orders:
            foods.add(o[2])
            if o[1] in tables:
                tables[o[1]].update([o[2]])
            else:
                tables[o[1]] = Counter([o[2]])

        sorted_foods = sorted(list(foods))
        food_index = {e: i for i, e in enumerate(sorted_foods)}

        sorted_tables = sorted(list(map(int, tables.keys())))
        final = []
        final.append(["Table"] + sorted_foods)
        for t in sorted_tables:
            t = str(t)
            c_food = ["0"]*len(sorted_foods)
            for f in tables[t]:
                c_food[food_index[f]] = str(tables[t][f])
            final.append([str(t)] + c_food)

        return final


s = Solution()
s.displayTable([["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"], [
               "Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]])
