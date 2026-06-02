class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # approach: binary search the sorted array
        
        def bin_s(left, right):
            # stop case
            if left > right: 
                return -1
                
            mid = (left + right) // 2

            # just right 
            if nums[mid] == target:
                return mid
            # too big
            if nums[mid] > target:
                return bin_s(left, mid-1)
            # too small
            if nums[mid] < target: 
                return bin_s(mid+1, right)
        
        return bin_s(0, len(nums)-1)


        # def binary(nums, absolute_index):
        #     # base case: if len = 0
        #     if len(nums) == 0:
        #         return -1
            
        #     # get middle index, check if greater or less
        #     i = len(nums) // 2

        #     # if equal
        #     if (nums[i] == target):
        #         return i + absolute_index
        #     # if smaller
        #     elif (nums[i] < target):
        #         return binary(nums[i+1:], i + absolute_index + 1)
        #     # if greater
        #     elif (nums[i] > target):
        #         return binary(nums[0:i], absolute_index)
        
        # return binary(nums, 0)

        # LO HI method of binary search:
    #     class Solution(object):
    # def search(self, nums, target):
    #     lo, hi = 0, len(nums) - 1
    #     while lo <= hi:
    #         mid = (lo + hi) // 2
    #         if nums[mid] == target:
    #             return mid
    #         elif nums[mid] < target:
    #             lo = mid + 1
    #         else:
    #             hi = mid - 1
    #     return -1