import math

class Solution:
    # piles[i]: is the number of bananas in the ith pile
    # h: number of hours to each all the bananas
    # return k: bananas / hr
    # constraint: each hour, can only eat k bananas from 1 pile. If the pile has less than k bananas
    # can't move on to the next pile in the same hour
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        res = r

        while l <= r:
            k = l + (r - l) // 2
            time_spent = 0

            for pile in piles:
                time_in_pile = math.ceil(pile / k)
                time_spent += time_in_pile
                # print("time_in_pile: ", pile, time_in_pile)

            # print("time_spent: ", time_spent, "h: ", h)
            # print("") 

            if time_spent <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res

        # min_k = 1
        # max_k = max(piles)
        # for k in range(min_k, max_k + 1):
        #     # print("k: ", k)
        #     time_spent = 0
        #     for pile in piles:
        #         time_in_pile = math.ceil(pile / k)
        #         time_spent += time_in_pile
        #         # print("time_in_pile: ", pile, time_in_pile)

        #     # print("time_spent: ", time_spent, "h: ", h)
        #     # print("") 

        #     if time_spent <= h:
        #         return k

        # return k