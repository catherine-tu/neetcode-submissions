class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # approach: DP, check for largest of previous numbers

        dp = [1] * len(nums)

        for i, num in enumerate(nums):
            for j in range(i):
                # check for previous larger sequences of smaller nums
                if nums[j] < num:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
            
        