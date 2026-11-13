
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Monotonic deque
        dq = deque()

        left = 0
        cost = 0
        ans = 0

        for right in range(n):

            # Maintain decreasing order in deque
            while dq and nums[dq[-1]] <= nums[right]:
                j = dq.pop()

                prev = dq[-1] if dq else left - 1

                cost -= nums[j] * (j - prev)

            dq.append(right)

            prev = dq[-2] if len(dq) > 1 else left - 1

            cost += nums[right] * (right - prev)

            # Shrink window if operations exceed k
            while cost > k:
                if dq and dq[0] == left:
                    dq.popleft()

                left += 1

                cost = 0
                prev = left - 1

                for j in dq:
                    cost += nums[j] * (j - prev)
                    prev = j

            # Count valid subarrays ending at right
            ans += right - left + 1

        return ans
