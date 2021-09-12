import time
import random
from os import system, name
# define our clear function
def clear():
  
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')
  
board = 10*[" "] 

##############

def display_board():
    
    global board
    print("     |     |     ")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
    print("     |     |      ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print("     |     |      ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")
    print("     |     |      ")
    
################

def check_position_is_empty(location):
    global board
    if board[location] == " ":
        return True
    return False

##################


def check_win():
    
    global board
    
    if(board[1] == board[2] == board[3] and board[1] != " "):    
        return True
    if(board[4] == board[5] == board[6] and board[4] != " "):    
        return True
    if(board[7] == board[8] == board[9] and board[7] != " "):    
        return True
    if(board[1] == board[4] == board[7] and board[1] != " "):    
        return True
    if(board[2] == board[5] == board[8] and board[2] != " "):    
        return True
    if(board[3] == board[6] == board[9] and board[3] != " "):    
        return True
    if(board[1] == board[5] == board[9] and board[1] != " "):    
        return True
    if(board[3] == board[5] == board[7] and board[3] != " "):    
        return True
    else:
        return False
    
def check_draw():
    global board
    for i in range(1,10):
        if board[i] == " ":
            return False
    return True


def main():
    print("\t****Welcome to Tic Toc Toe Game***")
    time.sleep(2)
    clear()
    
    print("the arm of player 1 is : X ")
    print("the arm of player 2 is : O ")
    time.sleep(2)   
    player = random.randint(0,1)
    while True :
        clear()    
        if(player % 2 != 0):    
            print("Player 1's chance , you are X")    
            mark = "X"    
            
        else:    
            print("Player 2's chance , you are O")    
            mark = "O"
            
        location = int(input("please choose one of the empty locations between(1 , 9) : "))  
        clear()
        if check_position_is_empty(location) == False:
            print("this location is Full !!!!!")
            display_board()
            time.sleep(3)
            continue

        board[location]= mark        
        display_board()
        time.sleep(3)
        
        if check_win() == True:
            print(f"the player with {mark} arm ,\n\n****** you win!!!! ******")
            time.sleep(3)
            break
            
            
        elif check_draw()==True:
            print ("Game Draw")
            time.sleep(3)
            break
        
        player+=1

if __name__ == '__main__':
    main()