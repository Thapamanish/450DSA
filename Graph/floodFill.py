class Solution:
    def floodFill(self, image, sr, sc, newColor):
        prevC = image[sr][sc]
        if prevC == newColor:
            return image
        self.floodFillUtil(image, sr, sc, prevC, newColor)
        return image
        
    def floodFillUtil(self, image, sr, sc, prevC, newC):
        
        if image[sr][sc] == prevC:
            image[sr][sc] = newC
            if sr >= 1: self.floodFillUtil(image, sr-1, sc, prevC, newC)
            if sr + 1 < len(image): self.floodFillUtil(image, sr+1, sc, prevC, newC)
            if sc >= 1: self.floodFillUtil(image, sr, sc - 1, prevC, newC)
            if sc + 1 < len(image[0]): self.floodFillUtil(image, sr, sc + 1, prevC, newC)
    


sol = Solution()

image = [[1,1,1],
         [1,1,0],
         [1,0,1]]


x = 1
y = 1
newC = 2

print(sol.floodFill(image, x, y, newC))