import os    
import time

board = 10*[""] 


########### flags

win = 1
game = 0
draw = -1
stope = 1   
##############
def display_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
################
def check_position_is_empty(Location):
    if board[Location] == "":
        return True
    return False

##################


def check_win():
    
    if(board[1] == board[2] == board[3] and board[1] != ' '):    
        return True
    if(board[4] == board[5] == board[6] and board[1] != ' '):    
        return True
    if(board[7] == board[8] == board[9] and board[1] != ' '):    
        return True
    if(board[1] == board[4] == board[7] and board[1] != ' '):    
        return True
    if(board[2] == board[5] == board[8] and board[1] != ' '):    
        return True
    if(board[3] == board[6] == board[8] and board[1] != ' '):    
        return True
    if(board[1] == board[5] == board[9] and board[1] != ' '):    
        return True
    if(board[3] == board[5] == board[7] and board[1] != ' '):    
        return True
    else:
        return False
    

    