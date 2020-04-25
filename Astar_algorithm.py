import pdb

class Grid:
    def __init__(self,size):
        self.n = size
        self.open = []
        self.closed = []

    def accept_puzzle(self):
        puzzle = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puzzle.append(temp)
        return puzzle

    def find(self,data,x):
        for i in range(0,len(data)):
            for j in range(0,len(data)):
                if data[i][j] == x:
                    return i,j

    def make_move(self,puzzle,x1,y1,x2,y2):
        if x2 >= 0 and x2 < self.n and y2 >=0 and y2 < self.n:
            temp = self.copy(puzzle)
            temp2 = temp[x2][y2]
            temp[x2][y2]= temp[x1][y1]
            temp[x1][y1] = temp2
            return temp
        else:
            return None
        
    def copy(self,root):
            """ Copy function to create a similar matrix of the given node"""
            temp = []
            for i in root:
                t = []
                for j in i:
                    t.append(j)
                temp.append(t)
            return temp
        
    def get_next_level(self, data):
        #Getting the empty space
        x,y = self.find(data,'_')

        #Getting the move list
        moves = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]

        #Children's list
        children = []
        for i in moves:
            child = self.make_move(data,x,y,i[0],i[1])
            if child is not None:
                children.append(child)
        return children

    def f(self,data,goal,g):
        return self.h(data,goal)+g

    def h(self,data,goal):
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if data[i][j] != goal[i][j] and data[i][j] != '_':
                    temp += 1
        return temp



    def get_index(self,x,fs,children):
        children.index(x)
        
    def solve_grid(self):
        #initiazling grids
        start_grid = self.accept_puzzle()
        goal_grid = [['1','2','3'],['4','5','6'],['7','8','_']]
        #initializing g
        g = 0
        self.open.append(start_grid)
        print("\n")
        fvals = []
        all_children = []
        while True:
            current = self.open[0]
            #Displaying the current grid
            print("")
            print("   |")
            print("   |")
            print("  \_/ \n")
            for i in current:
                for j in i:
                    print(j, end = " ")
                print("")
            if(self.h(current,goal_grid) == 0):
                break
            children = self.get_next_level(current)
            for i in children:
                all_children.append(i)
                f_value = self.f(i,goal_grid,g)
                fvals.append(f_value)
                self.open.append(i)
            g+=1
            self.closed.append(current)
            del self.open[0]
            self.open.sort(key = lambda x : fvals[all_children.index(x)])
            



grid = Grid(3)
grid.solve_grid()
