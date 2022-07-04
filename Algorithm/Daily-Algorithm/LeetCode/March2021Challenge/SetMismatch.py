class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        li = [0]*len(nums)

        n = 0

        while nums: #O(n)
            top = nums.pop() #O(1)
            if li[top-1] == 1:
                n = top
            else:
                li[top-1] = 1
        
        for i in range(0, len(li)):
            if li[i] == 0:
                return [n, i+1]

