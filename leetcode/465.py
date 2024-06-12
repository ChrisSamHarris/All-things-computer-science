# You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.
# Return the minimum number of transactions required to settle the debt.

# Example 1:
# Input: transactions = [[0,1,10],[2,0,5]]
# Output: 2
# Explanation:
# Person #0 gave person #1 $10.
# Person #2 gave person #0 $5.
# Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

# Example 2:
# Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
# Output: 1
# Explanation:
# Person #0 gave person #1 $10.
# Person #1 gave person #0 $1.
# Person #1 gave person #2 $5.
# Person #2 gave person #0 $5.
# Therefore, person #1 only need to give person #0 $4, and all debt is settled.
from collections import defaultdict

class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        
        # Step 1: Calculate net balance for each person
        balance = defaultdict(int)
        for fr, to, amt in transactions:
            balance[fr] -= amt
            balance[to] += amt

        # Step 2: Filter out people with zero balance and create a list of debts
        debts = list(balance.values())
        debts = [x for x in debts if x != 0]

        # Helper function to perform the recursive search for minimum transactions
        def dfs(start):
            while start < len(debts) and debts[start] == 0:
                start += 1
            if start == len(debts):
                return 0
            min_trans = float('inf')
            for i in range(start + 1, len(debts)):
                if debts[i] * debts[start] < 0:
                    debts[i] += debts[start]
                    min_trans = min(min_trans, 1 + dfs(start + 1))
                    debts[i] -= debts[start]
            return min_trans

        return dfs(0)

# Example usage
transactions1 = [[0,1,10],[2,0,5]]
transactions2 = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]

solution = Solution()
print(solution.minTransfers(transactions1)) # Output: 2
print(solution.minTransfers(transactions2)) # Output: 1