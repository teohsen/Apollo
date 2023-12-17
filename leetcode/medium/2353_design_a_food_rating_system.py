from typing import List
from sortedcontainers import SortedSet
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        """
        # Time - O(nlogn)
        :param foods:
        :param cuisines:
        :param ratings:
        """
        self.od = defaultdict(SortedSet)
        self.c = dict(zip(foods, cuisines))
        self.r = dict(zip(foods, ratings))

        for i in range(len(foods)):
            self.od[cuisines[i]].add((-ratings[i], foods[i]))  # -ratings[i] for descending order
            # self.c[foods[i]] = cuisines[i]
            # self.r[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        """
        # Time - O(logn)
        :param food:
        :param newRating:
        :return:
        """
        c = self.c.get(food)
        r = self.r.get(food)
        self.od[c].remove((-r, food))
        self.od[c].add((-newRating, food))
        self.r[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        """
        # Time - O(1)

        :param cuisine:
        :return:
        """
        return self.od[cuisine][0][1]


class FoodRatings2:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.od = dict(zip(foods, [list(_) for _ in zip(cuisines, ratings)]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.od[food][1] = newRating

    def highestRated(self, cuisine: str) -> str:
        best = None
        best_score = -1
        for k, v in self.od.items():
            if v[0] == cuisine:
                if v[1] >= best_score:
                    if v[1] == best_score:
                        if k > best:
                            continue

                    best = k
                    best_score = v[1]

        return best


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
