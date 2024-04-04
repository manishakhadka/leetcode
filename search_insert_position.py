# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

class Solution():
    def searchInsert(self, nums, target):
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

s1= Solution()
nums1, target1 = [1, 3, 5, 6], 5
nums2, target2 = [1, 3, 5, 6], 2
nums3, target3 = [1, 3, 5, 6], 7

print(s1.searchInsert(nums1, target1))  
print(s1.searchInsert(nums2, target2)) 
print(s1.searchInsert(nums3, target3))  
                