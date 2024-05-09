'''
	There are two sorted arrays nums1 and nums2 of size m and n respectively.

	Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

	Example 1:
	nums1 = [1, 3]
	nums2 = [2]

	The median is 2.0
	Example 2:
	nums1 = [1, 2]
	nums2 = [3, 4]

	The median is (2 + 3)/2 = 2.5
'''
# Took 96 ms as O(m+n)
def findMedianSortedArrays(nums1, nums2) -> float:
    full_ar = sorted(nums1+nums2)
    length = len(full_ar)
    if length%2 == 1:
        return full_ar[int((length/2) - 0.5)]
    else:
        return (full_ar[int((length/2)-1)] + full_ar[int((length/2))]) / 2

# Took 73 ms as O(log(m+n))
def findMedianSortedArrays(nums1, nums2) -> float:
    # Keeping the first array as small to make the algorithm works to avoid multiple conditions
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partition_x = int((low + high)/2)
        # reducing partition_x value to make the partition_y move towards median as we increment partition_x
        partition_y = int((x+y+1) / 2 - partition_x)

        if partition_x == 0:
            maxLeftX = float('-inf')
        else:
            maxLeftX = nums1[partition_x-1]

        if partition_x == x:
            minRightX = float('inf')
        else:
            minRightX = nums1[partition_x]

        if partition_y == 0:
            maxLeftY = float('-inf')
        else:
            maxLeftY = nums2[partition_y-1]

        if partition_y == y:
            minRightY = float('inf')
        else:
            minRightY = nums2[partition_y]
        # maxleftx minleftx minrighty maxrighty
        # < {   } >
        # leftx righty lefty rightx
        # <}{> -- Intercrossed gives the median or keep x at edge and keep reducing the y.
            
        #0 1, 2, 3    4, 5, 6, 7, 8, 9, 10, 11, 12, 13
        #1 <  x  {             }  y  >
        #2    <  x  {        }  y  >
        #3 minrightx becomes infinity its enter the actual condition
        #4 since it is odd, max(2, 6) + min(infinity, 8) = 6 + 8 / 2 = 7 
        if maxLeftY <= minRightX and maxLeftX <= minRightY:
            if (x+y)%2 == 0:
                # Taking the max of left most value + Taking min of right most value from median divide by 2
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            else:
                # Two closest values of median
                return max(maxLeftY, minRightX)
            
        if maxLeftX > minRightX:
            high = partition_x - 1
        else:
            low = partition_x + 1

'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''
# https://leetcode.com/problems/container-with-most-water/description/

def container_with_most_water(height):
    # Having a two pointer way, and starting from the two most edges
    left, right, max_area = 0, len(height) - 1, 0
    # Iterate complete bars and saving the maxarea along the way
    while left < right:
        max_area = max(
            max_area,
            min(height[left], height[right]) * (right-left)
            )
        # The minimum bar height will always determine the max area
        # Hence increasing the minimum one
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


'''
	Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array 
    which gives the sum of zero.

	Note:

	The solution set must not contain duplicate triplets.

	Example:

	Given array nums = [-1, 0, 1, 2, -1, -4],

	A solution set is:
	[
	  [-1, 0, 1],
	  [-1, -1, 2]
	]
    https://leetcode.com/problems/3sum/
'''
def threeSum(nums):
        nums.sort()

        # Handling 0s from the input list
        if len(nums) >= 3 and nums[0] == nums[-1] and nums[0] == 0:
            return [[0, 0, 0]]
        
        triplets = []
        for index in range(len(nums) - 1):
            # Assigning left, index, right makes no equal values as per description
            left = index + 1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[index] + nums[left] + nums[right]

                if cur_sum == 0:
                    triplets.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                elif cur_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        # Using set function(converting list to tuple(hashable)) to get the unique triplets 
        return [list(unique_triplet) for unique_triplet in set(tuple(triplet) for triplet in triplets)]

# ---------------------------------------------- Inference--------------------------
print(findMedianSortedArrays([1,2], [3]))
        