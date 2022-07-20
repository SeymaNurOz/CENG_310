"""
Created on Wed Apr 13 15:49:40 2022

@author: seyma"""

class Empty(Exception):
    pass

class Stack():
    def __init__(self):
        self._st=[]
        
    def __len__(self):
        return len(self._st)
    
    def isempty(self):
        return len(self._st)==0
        
    def push(self,element):
        self._st.append(element)
        
    def pop(self):
        if self.isempty():
            raise Empty("Stack is empty")
        else:
            return self._st.pop()
            
    def top(self):
        if self.isempty():
            raise Empty("Stack is empty")
        else:
            return self._st[-1]
                
class Queue():
    def __init__(self):
        self._q=[]
        
    def __len__(self):
        return len(self._q)
    
    def isempty(self):
        return len(self._q)==0
    
    def front(self):
        if self.isempty():
            raise Empty("Queue is empty")
        else:
            return self._q[0]
        
    def enqueue(self,element):
        self._q.append(element)
        
    def dequeue(self):
        if self.isempty():
            raise Empty("Queue is empty")
        else:
            return self._q.pop(0)
          
    
def try_paths(grid,cur_x,cur_y):
    if cur_x<len(grid)-1:
        if grid[cur_x+1][cur_y]==1:
            return [cur_x+1,cur_y]
    if cur_y<len(grid[0])-1:
        if grid[cur_x][cur_y+1]==1:
            return [cur_x,cur_y+1]
    if cur_x>0:
        if grid[cur_x-1][cur_y]==1:
            return [cur_x-1,cur_y]
    if cur_y>0:
        if grid[cur_x][cur_y-1]==1:
            return [cur_x,cur_y-1]
    else:
        return None


        
def solve_stack(stack_x):
    reverse_stack=Stack()
    while not stack_x.isempty():
        reverse_stack.push(stack_x.pop())
    while not reverse_stack.isempty():
        x=str(reverse_stack.pop())
        print(x[:3]+x[4:])

    
    
def pathFinder(grid, startX, startY, endX, endY):
    path_stack=Stack()
    path_stack.push([startX,startY])
    
    # for i in range(5):
    while not path_stack.isempty():
        [cur_x,cur_y]=path_stack.top()
        
        
        if [cur_x,cur_y]==[endX,endY]:
            return solve_stack(path_stack)
    
        else:     
            rs=try_paths(grid,cur_x,cur_y)
            # print(rs)
            if rs!=None:
                [cur_x,cur_y]=rs
                grid[cur_x][cur_y]=0
                path_stack.push([cur_x,cur_y])
            else:
                path_stack.pop()
                
    return print("Path not found")

# pathFinder([[1,1,1,0,1],[1,1,0,0,1],[1,0,1,1,1],[1,0,0,1,0],[1,1,1,1,0]], 2, 2, 0, 4)
# pathFinder([[1,1,1,0,1],[1,1,0,0,1],[1,0,1,1,1],[1,0,0,1,0],[1,1,1,1,0]], 2, 2, 0, 1)
pathFinder([[1,1,1,0,1],[1,1,0,0,1],[1,0,1,1,1],[1,0,0,1,0],[1,1,1,1,0]], 2, 2, 0, 3)
pathFinder([[1,1,1,0,1],[1,1,0,0,1],[1,0,1,1,1],[1,0,0,1,0],[1,1,1,1,0]], 2, 2, 4, 4)
# pathFinder([[1,1,1,0,1],[1,1,0,0,1],[1,0,1,1,1],[1,0,0,1,0],[1,1,1,1,0]], 2, 2, 4, 0)
# pathFinder([[1,1,1,0,1],[1,1,0,0,1],[1,0,1,1,1],[1,0,0,1,0],[1,1,1,1,0]], 2, 2, 3, 3)
# pathFinder([[1,1,1,0,1],[1,1,0,0,1],[1,0,1,1,1],[1,0,0,1,0],[1,1,1,1,0]], 2, 2, 0, 0)



