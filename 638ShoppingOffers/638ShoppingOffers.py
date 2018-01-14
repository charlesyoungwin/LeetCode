class Solution:

    #time limit exceeded, optimize the code
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def helper(needs):
            # for elem in needs:
            #     if elem < 0:
            #         return 
            # if any(needs) == False:
            #     nonlocal res
            #     res = min(res, value)
            # for item in special: 
            #     flag = 0
            #     for i in range(len(needs)):
            #         if needs[i] < item[i]:
            #             flag = 1
            #             break
            #     if flag == 1:
            #         continue
            #     tmp = [needs[i] - item[i] for i in range(len(needs))]
            #     helper(tmp, value + item[i+1])
            local_min = sum(needs[i] * price[i] for i in range(len(needs)))
            for spec in special:
                tmp = [needs[i] - spec[i] for i in range(len(needs))]
                if min(tmp) < 0:
                    tmp = None
                if tmp:
                    local_min = min(local_min, helper(tmp) + spec[-1])
            return local_min

        return helper(needs)

    def shoppingOffersV2(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        d = {}
        def helper(cur):
            val = sum(cur[i] * price[i] for i in range(len(needs)))
            for spec in special:
                tmp = [cur[j] - spec[j] for j in range(len(needs))]
                if min(tmp) >= 0:
                    val = min(val, d.get(tuple(tmp), helper(tmp)) + spec[-1])
            d[tuple(tmp)] = val
            return val
        return helper(needs)

if __name__ == '__main__':
    prices = [2, 5]
    special = [[3, 0, 5], [1, 2, 10]]
    needs = [3, 2]
    print(Solution().shoppingOffers(prices, special, needs))



