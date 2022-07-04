class Solution:
    def distributeCandies(self, candyType):
        n = len(candyType)
        candyType = list(set(candyType))
        candy_num = len(candyType)

        if candy_num <= int(n/2):
            self.result = candy_num
        else:
            self.result = int(n/2)
        
        return self.result
        