class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        last_index = {}
        baskets = set()
        res = 0
        for r in range(len(fruits)):

            last_index[fruits[r]] = r

            if len(baskets) == 2 and fruits[r] not in baskets:
                min_index = len(fruits)
                for f in baskets:
                    min_index = min(last_index[f], min_index)
                
                baskets.remove(fruits[min_index])

                l = min_index + 1

            baskets.add(fruits[r])

            res = max(res, r - l + 1)

        return res


