class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):    
            ans = target - nums[i] 
            for j in range(i + 1, len(nums)):
                if ans == nums[j]:
                    return [i , j]
        return None

