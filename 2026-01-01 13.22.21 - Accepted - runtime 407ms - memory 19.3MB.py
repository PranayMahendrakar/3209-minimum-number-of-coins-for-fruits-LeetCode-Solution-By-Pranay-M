class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i] = minimum cost to acquire fruits 1 to n, starting from fruit i+1
        # If we buy fruit i (0-indexed), we get fruits i+1 to min(n-1, i + i + 1) free
        
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def dp(i):
            if i >= n:
                return 0
            
            # Must buy fruit i, which gives us fruits i+1 to i+i+1 free (0-indexed)
            # So next fruit we need to consider is from i+1+1 to 2*i+2
            cost = prices[i]
            # After buying fruit i, we can start next purchase from i+2 to 2*(i+1)+1
            min_next = float('inf')
            for j in range(i + 1, min(2 * (i + 1) + 1, n + 1)):
                min_next = min(min_next, dp(j))
            
            return cost + (min_next if min_next != float('inf') else 0)
        
        return dp(0)