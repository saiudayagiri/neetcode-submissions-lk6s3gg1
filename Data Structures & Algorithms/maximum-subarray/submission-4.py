class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_arr_sum = nums[0]
        cur_sub_arr_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sub_arr_sum = max(cur_sub_arr_sum + nums[i], nums[i])
            max_sub_arr_sum = max(max_sub_arr_sum,cur_sub_arr_sum )
        return max_sub_arr_sum
        