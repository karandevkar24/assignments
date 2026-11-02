def find_paths(grid,row,col,path,paths):
    if row==len(grid)-1 and col==len(grid)-1:
        paths.append(path)
        return
    if row<len(grid):
        find_paths(grid,row+1,col,path+"D",paths)
    if col<len(grid):
        find_paths(grid,row,col+1,path+"R",paths)
def first_10(paths):
    for i in range(10):
        print(i,":",paths[i])

n=int(input())
grid =[[0 for j in range(n)] for i in range(n)]
paths=[]
find_paths(grid,0,0,"",paths)
print("total number of possible paths:",len(paths))
first_10(paths)
