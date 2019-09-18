# PS2.py: Program to play 3X3 Numeric Tic-Tac-Toe.
# Author: Parveen Bajaj

import sys

def winner_test(matrix):
    # Horizontal Sum Check
    temp = 0;
    
    for row in matrix:
        if sum(row) == 15:
            return True
           
    # Vertical Sum Check
    for i in range(3):
        if sum([x[i] for x in matrix])==15:
            return True
           
    # Diagonal Sum Check
    total = matrix[0][0] + matrix[1][1] + matrix[2][2]
    if total == 15:
        
        return True
    
    total = matrix[0][2] + matrix[1][1] + matrix[2][0]
    if total == 15:
        return True
    
    return False    

if __name__ == "__main__":
    
    matrix = [[0,0,0],[0,0,0],[0,0,0]]
    print "Welcome to the Game!"

    odd_set = ['1','3','5','7','9']
    even_set = ['2','4','6','8']
    
    turn = 1;
    
    while(True):
    
        if turn == 1:
            
            print "Player 1’s chance"
    
            P_N = raw_input("Enter the position and number to be entered:")
            
            P_N = P_N.split(',')
            
            Position = int(P_N[0])
            
            Number = int(P_N[1])
                
            #Check for constrains for Player 1
            if (Position < 0  or Position >9) :
                print "Invalid Position"
                continue
            
            if not(str(Number) in odd_set):
                print "Invalid Number"
                continue
            
            matrix[(Position-1)/3][(Position-1)%3] = Number
            
            print matrix
            
            if winner_test(matrix):
                print "Player 1 is winner"
                exit()
                        
            turn = 2
            
        else:
            
            print "Player 2’s chance"
    
            P_N = raw_input("Enter the position and number to be entered:")
            
            P_N = P_N.split(',')
            
            Position = int(P_N[0])
            
            Number = int(P_N[1])
            
                  
            print Position
            
            print Number
            
            #Check for constrains for Player 1
            if (Position < 0  or Position >9) :
                print "Invalid Position"
                continue
            
            if not(str(Number) in even_set):
                print "Invalid Number"
                continue
            
            turn = 1
            
            matrix[(Position-1)/3][(Position-1)%3] = Number
            
            print matrix 
            
            if winner_test(matrix):
                print "Player 2 is winner"
                exit()
            
        
        
