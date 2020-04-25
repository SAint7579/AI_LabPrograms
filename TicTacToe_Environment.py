##Class for the environment
import numpy as np

#Defining variables
LENGTH = 3


class Environment:
    def __init__(self):
        self.board = np.zeros((LENGTH,LENGTH))
        self.x = -1.0
        self.o = 1.0
        self.winner = None
        self.ended = False        
        
    def is_empty(self,i,j):
        '''
            Checks if a place is empty
        '''
        return self.board[i,j]==0
    
    
    def reward(self,sym):
        # no reward until the game is over
        if not self.game_over():
            return 0
        
        #if we get here, game is over
        #sym will be self.x or self.o
        if self.winner == sym:
            return 1
        elif self.winner == sym*-1:
            return -1
        elif self.winner == None:
            return 0
    
    def game_over(self, force_recalculate= False):
        if not force_recalculate and self.ended:
            return self.ended
        
        #For rows
        for i in range(LENGTH):
            for player in (self.x, self.o):
                #Sum will be -3 for x and +3 for 0
                if self.board[i].sum() == player*LENGTH:
                    self.winner = player
                    self.ended = True
                    return True
        #For columns
        for j in range(LENGTH):
            for player in (self.x, self.o):
                #Sum will be -3 for x and +3 for 0
                if self.board[:,j].sum() == player*LENGTH:
                    self.winner = player
                    self.ended = True
                    return True
        
        #For diagonals
        for player in (self.x,self.o):
            #top-left -> bottom-right diagonal
            if self.board.trace() == player*LENGTH:
                self.winner = player
                self.ended = True
                return True
            
            #top-right -> bottom-left diagonal
            if np.fliplr(self.board).trace() == player*LENGTH:
                self.winner = player
                self.ended = True
                return True
        #For draws
        if np.all((self.board==0) == False):
            self.winner = None
            self.ended= True
            return True
        
        #not over
        self.winner = None
        return False
    
    def draw_board(self):
        for i in range(LENGTH):
            print("-------------")
            for j in range(LENGTH):
                print("  ", end="")
                if self.board[i,j] == self.x:
                    print("x ", end="")
                elif self.board[i,j] == self.o:
                    print("o ", end="")
                else:
                    print("  ", end="")
            print("")
        print("-------------")
            

                    
    

                
                
