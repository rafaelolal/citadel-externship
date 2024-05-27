from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        table = [-1]*(len(nums))
        table[0] = 0
        table[1] = nums[0]

        self.dp(nums[:-1], len(nums)-1, table)

        r1 = table[-1]

        table = [-1]*(len(nums))
        table[0] = 0
        table[1] = nums[0]

        self.dp(nums[1:], len(nums)-1, table)

        r2 = table[-1]
        return max(r1, r2)

    def dp(self, nums, i, table):
        if table[i] != -1:
            return table[i]

        table[i] = max(
            self.dp(nums, max(0, i-2), table) + nums[i-1],
            self.dp(nums, max(0, i-1), table)
        )

        return table[i]


s = Solution()
print(s.rob([1, 2, 3, 1]))
