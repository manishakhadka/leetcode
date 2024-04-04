# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?



class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        num_indices = {}
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
            # If the complement exists in the dictionary, return its index along with the index
            if complement in num_indices:
                return [num_indices[complement], i]
            # Otherwise, store the index of the current element in the dictionary
            num_indices[num] = i

        # If no solution is found, return None
        return None

# Create an instance of Solution
s1 = Solution()
# Define the input parameters
nums = [2, 7, 11, 15]
target = 9
# Call the twoSum method using the instance
print(s1.twoSum(nums, target))  