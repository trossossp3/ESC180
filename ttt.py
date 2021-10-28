'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random
from copy import deepcopy
# global board
# board =


def init():

    global arr
    arr = []


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " + board[i][0] + " | " + board[i][1] + " | " + board[i][2]
        line2 = "  " + str(3*i+1) + " | " + str(3*i+2) + " | " + str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")


def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

# converts a value 1-9 to a coord for the grid
def input_location(square_num):
    if(square_num < 1 or square_num > 9):
        return
    row_num = ((square_num-1)//3)
    if square_num % 3 == 0:
        col_num = 2
    elif square_num % 3 == 2:
        col_num = 1
    else:
        col_num = 0
    return row_num, col_num

# checks if three elements are diagonal
def check_diagonal(board):
    return board[0][0]==board[1][1] and board[0][0] == board[2][2] and board[0][0]!=" "

def is_win(board):
    # checks if the same three elements are in a row
    for i in range(3):
        if board[i].count(board[i][0]) == len(board) and board[i][0]!=" ":
            return True
        arr = []
        # checks if three elemets are in same column
        for j in range(3):
            arr.append(board[j][i])
        if arr.count(arr[0]) == len(board) and arr[0]!=" ":
            return True
    return False or check_diagonal(board)




def put_in_board(mark, square_num, board):

    x, y = input_location(square_num)
    board[x][y] = mark

# chcks if good input and hasnt been done
def good_input(input, arr):
    if (int(input) < 1 or int(input) > 9):
        return False
    if(input in arr):
        return False
    return True


def play_game(board):
    game_over = False
    arr = []
    while not game_over:
        print("Player 1 input")
        input1 = input()
        while(not good_input(str(input1), arr)):
            print("try again")
            input1 = input()
        arr.append(input1)
        put_in_board("X", int(input1),board)
        print_board_and_legend(board)
        if(is_win(board)):
            game_over = True
            print("player 1 won")
            return
        get_free_squares(board)
        print("Player 2 input")
        input2 = input()
        while(not good_input(str(input2), arr)):
            print("try again")
            input2 = input()
        arr.append(input2)
        put_in_board("O", int(input2), board)
        print_board_and_legend(board)
        if(is_win(board)):
            game_over = True
            print("player 2 won")
            return

def get_free_squares(board):
    global arr
    arr = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                arr.append([i,j])
# converst a coordinate ([1,2]) to a number 1-9
def coors_to_number(ar):
    if ar[0] ==0:
        return 1 + ar[1]
    elif ar[0] ==1:
        return 4 + ar[1]
    else:
        return 7 + ar[1]


def make_random_move(board):
    get_free_squares(board)
    index_coors = random.choice(arr)
    index = coors_to_number(index_coors)
    print(index)
    return index

def play_computer(board):
    
    game_over = False
    arr = []
    while not game_over:
        print("Player 1 input")
        input1 = input()
        while(not good_input(str(input1), arr)):
            print("try again")
            input1 = input()
        arr.append(input1)
        put_in_board("X", int(input1), board)
        print_board_and_legend(board)
        if(is_win(board)):
            game_over = True
            print("player 1 won")
            return       
        # index = int(make_random_move())
        index = brute_force()
        arr.append(index)
        put_in_board("O", int(index), board)
        print_board_and_legend(board)
        if(is_win(board)):
            game_over = True
            print("Computer won")
            return

# checks if computer can win that turn if not random placement
def brute_force():
 
    for i in arr:
        board_temp = deepcopy(board)
        put_in_board("O", int(coors_to_number(i)), board_temp)
        if(is_win(board_temp)):
            return int(coors_to_number(i))
            
    else:
        return int(make_random_move(board))
        
if __name__ == '__main__':
    init()
    board = make_empty_board()
    print_board_and_legend(board)
    # play_game(board)
    play_computer(board)
    print("\n\n")

    # board = [["O", "X", "X"],
    #          [" ", "X", " "],
    #          [" ", "O", " "]]

    print_board_and_legend(board)
