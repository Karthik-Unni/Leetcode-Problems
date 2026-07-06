class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

# Since the majority element appears more than half the time,
# after sorting it will always include the middle index.
# Therefore, the middle element is the majority element.