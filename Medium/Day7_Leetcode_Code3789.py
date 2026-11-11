
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        cost1_option = need1 * cost1 + need2 * cost2

        cost2_option = (
            min(need1, need2) * costBoth
            + max(0, need1 - need2) * cost1
            + max(0, need2 - need1) * cost2
        )

        cost3_option = max(need1, need2) * costBoth

        return min(cost1_option, cost2_option, cost3_option)
