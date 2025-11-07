from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        bal = []
        for acc in accounts:
            bal.append(sum(acc))
        
        return max(bal)


if __name__ == "__main__":
    accounts_1 = [[1,2,3],[3,2,1]]
    accounts_2 = [[1,5],[7,3],[3,5]]
    accounts_3 = [[2,8,7],[7,1,3],[1,9,5]]

    s = Solution()
    o = s.maximumWealth(accounts_1)
    print(o)
