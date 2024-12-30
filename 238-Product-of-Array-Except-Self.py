class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num
        for i in range(len(nums)):
            if zero_count > 1:
                nums[i] = 0
            elif zero_count == 1:
                nums[i] = total_product if nums[i] == 0 else 0
            else:
                nums[i] = total_product // nums[i]

        return nums
