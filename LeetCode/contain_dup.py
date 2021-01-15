class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums = [1, 2, 3, 1]
        numsLen = len(nums)
        for i in range(numsLen - 1):
            # i = 0, 1...
            for j in range(i + 1, numsLen):
                print(i, ',', j)
                if nums[i] == nums[j]:
                    return True
        return False

