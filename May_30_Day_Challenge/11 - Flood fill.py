def mysoln_floodFill(image, sr, sc, newColor):
    # 80% faster
    start_color = image[sr][sc]
    visited = [[0]*len(image[0]) for _ in range(len(image))]
    
    # edge case; nothing is changed
    if start_color == newColor: return image

    def dfs(sr, sc):
        
        if sr < 0 or sr >= len(image):
            return
        elif sc < 0 or sc >= len(image[0]):
            return
        elif visited[sr][sc]:
            return
        
        if image[sr][sc] == start_color:
            image[sr][sc] = newColor
            
            visited[sr][sc] = 1
            
            dfs(sr-1, sc)
            dfs(sr+1, sc)
            dfs(sr, sc+1)
            dfs(sr, sc-1)

    dfs(sr, sc)
    return image

def discpage(image, sr, sc, newColor):
    # 100% faster --> remove visited array. Takes time to create

    # Keep DFS going forward and stop if the node is not of the original color 
    # (which means it's either wasn't meant to be visited or has already been visited and changed with the new color).

    # if the new color is the target node color then return it's already flooded 
    def ff(img, x, y, c, mcolor):
        valid =  x >= 0 and y >= 0 and x < len(img) and y < len(img[0]) and img[x][y] == mcolor
        if not valid:
            return
        img[x][y] = c
        ff(img, x + 1, y, c, mcolor)
        ff(img, x - 1, y, c, mcolor)
        ff(img, x, y + 1, c, mcolor)
        ff(img, x, y - 1, c, mcolor)
    
    if image[sr][sc] == newColor:
        return image
    ff(image, sr, sc, newColor, image[sr][sc])
    return image



