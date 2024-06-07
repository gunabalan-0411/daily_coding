'''
https://leetcode.com/problems/trapping-rain-water/
'''
def trap(height):
    # Brute Force algo
    # -- Its linear but uses extra memory
    # 1. calculate an array of maxLeft of each num from left to right
    # 2. Calculate an array of maxRight of each num from right to left
    # 3. Calculate an array of min(maxLeft, maxRight) as min determines the max water
    # 4. min(maxLeft, maxRight) - Height[i] >= 0 gives reduce the height of individual bar
    # 5. Now the sum of gives the total water content
    
    # O(N) Speed and O(N) Space
    if not height: return 0

    l, r = 0, len(height)-1
    maxLeft, maxRight = height[l], height[r]
    water = 0
    while l < r:
        if maxLeft < maxRight:
            l += 1
            maxLeft = max(maxLeft, height[l])
            water += maxLeft - height[l]
        else:
            r -= 1
            maxRight = max(maxRight, height[r])
            water += maxRight - height[r]
    return water