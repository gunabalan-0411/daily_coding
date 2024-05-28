class Solution:
    def search(self, nums, target) -> int:
        # 47 ms solution
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1
        # -- After rotation the graph of the formerly sorted array would be like
        # [3, 4, 5, 1, 2] when k = 2
        # |  /|
        # | / |
        # |/__|_____
        # |   | /
        # |___|/____
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            # left sorted portion
            # First search through in left sorted portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # right sorted portion
            else:
                # second condition is: in cases where we skip the left sorted portion 
                # like [5, 1, 3] hence check back in left sorted portion
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1