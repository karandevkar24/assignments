n=int(input())
row_move=[-2,-1,1,2,2,1,-1,-2]
col_move=[1,2,2,1,-1,-2,-2,-1]
grid=[[-1 for j in range(n)] for i in range(n) ]
def show_grid(grid):
    for row in grid:
        for value in row:
            print(value,end=" ")
        print()
show_grid(grid)
def is_valid(grid,row,col):
    if 0<=row<n and 0<=col<n and grid[row][col]==-1:
        return True
def knighttour(grid,start_row,start_col,count,stack):
    while count!=n*n:
        for i in range(stack[-1][2],8):
            new_row=start_row+row_move[i]
            new_col=start_col+col_move[i]

            if is_valid(grid,new_row,new_col):
                stack[-1]=(start_row,start_col,i+1)
                grid[new_row][new_col]=count
                stack.append((new_row,new_col,0))
                count+=1

                start_row=new_row
                start_col=new_col
                break
        else:
            popped=stack.pop()
            grid[popped[0]][popped[1]]=-1
            count-=1
            if stack:
                start_row=stack[-1][0]
                start_col=stack[-1][1]
            else:
                return False
    return True
stack=[(0,0,0)]
grid[0][0]=0
if knighttour(grid,0,0,1,stack):
    show_grid(grid)
    print("solution exist")
else:
    print("no solution exist")
