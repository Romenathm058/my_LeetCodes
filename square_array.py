
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        new = []

        nums.sort()

        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
            new.append(nums[i])
        new.sort()
        return new
        
