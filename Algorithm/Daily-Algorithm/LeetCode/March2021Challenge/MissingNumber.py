class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        li = [0]*(len(nums)+1)

        for i in range(len(nums)): # O(n)
            li[nums[i]] = 1
        
        for i in range(len(li)):
            if li[i] ==0:
                return i
        return len(nums)+1