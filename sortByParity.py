class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        new1=[]
        new2=[]

        for i in range(len(nums)):
            if(nums[i] %2 == 0):
                new1.append(nums[i])
            else:
                new2.append(nums[i])
        new1.sort()
        new2.sort()

        merge = new1 + new2

        return merge
        
        
