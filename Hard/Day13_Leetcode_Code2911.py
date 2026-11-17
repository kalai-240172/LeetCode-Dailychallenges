class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Step 1: Precompute semi-palindrome costs
        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                best = INF

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Compare characters in each group
                    for offset in range(d):
                        left = i + offset
                        right = i + offset + length - d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][i + length - 1] = best

        # Step 2: Dynamic Programming
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):
                for j in range(2 * (parts - 1), i - 1):

                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[j][parts - 1] + cost[j][i - 1]
                    )

        return dp[n][k]
