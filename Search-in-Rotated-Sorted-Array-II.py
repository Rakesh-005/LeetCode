class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search by identifying the sorted half.

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True
            if nums[mid] == nums[low]:
                low += 1
                continue
            # Check if left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False