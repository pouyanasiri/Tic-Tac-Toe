import time
import random
from os import stat, system, name

board = 10*[" "]

def clear():
  
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')
  

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
    

def check_position_is_empty(location):
    global board
    if board[location] == " ":
        return True
    return False


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

def menu():
    print("*************************")
    print("*          Menu         *")
    print("* 1 : Start new game    *")
    print("* 2 : Help              *")
    print("* 3 : Exit              *")
    print("*                       *")
    print("*************************")

    choice = int(input("please choose one of the choices : "))
    
    if choice== 1 :
        startgame()
    elif choice == 2 :
        help_game()
    elif choice == 3 :
        exit()
    else :
        menu()
        
def help_game():
    print("**********************************************************************************")
    time.sleep(1)
    print("*                      *** Description And Help ***                              *")
    time.sleep(1)
    print("* Tic Tac Toe in a project prepared by Pouya Nasiri                              *")
    time.sleep(1)
    print("* This game includes a 3 in 3 square.                                            *")
    time.sleep(1)
    print("* Victory condition : If you can make a straight line with 3 characters, you win *")
    time.sleep(1)
    print("* Equal condition : If no one can make a straight line, You draw                 *")
    time.sleep(1)
    print("**********************************************************************************")
    time.sleep(3)
    print("1 : Back   2 : Exit ")
    choice = int(input("please enter a choice : "))
    if choice == 1 :
        menu()
    elif choice == 2:
        exit()
    else :
        help_game()

def startgame():
    
    global board
    board = 10*[" "] 
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
        display_board()   
        location = int(input("please choose one of the empty locations between(1 , 9) : "))  
        if not 0<location<10:
            continue
        
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
            time.sleep(4)
            clear()
            break
            
            
        elif check_draw()==True:
            print ("Game Draw")
            time.sleep(4)
            clear()
            break
        
        player+=1

    menu()
    
def main():
    print("\t****Welcome to Tic Toc Toe Game***")
    
    time.sleep(2)
    clear()
    menu()
    clear()
    startgame()
    
if __name__ == '__main__':
    main()