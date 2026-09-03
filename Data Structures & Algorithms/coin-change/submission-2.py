class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        result = [float("inf")] * (amount + 1)
        result[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin: 
                    diff = i - coin 
                    result[i] = min(result[i], (1 + result[diff]))

        
        return result[-1] if result[-1] != float("inf") else -1