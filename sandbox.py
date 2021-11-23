"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 30, 2021
"""
a = "w"
b = "b"

L = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]]


def is_empty(board):
    for i in range(8):
        for k in range(8):
            if board[i][k] != " ":
                return False

    return True

def is_bounded(board, y_end, x_end, length, d_y, d_x):
#TRUE MEANS OPEN AND FALSE MEANS CLOSED
    top = True
    bottom = True
    colour = board[y_end][x_end]

    other_colour = None
    if colour == "w":
        other_colour = "b"
    elif colour == "b":
        other_colour = "w"


    #vertical case
    if d_y == 1 and d_x == 0:
        coordinates = [y_end - length, x_end]
        if coordinates not in L:
            top = False
        else:
            beginning = board[y_end - length][x_end]
            if beginning == other_colour:
                top = False

        coordinates_of_end = [y_end + 1, x_end]
        if coordinates_of_end not in L:
            bottom = False
        else:
             end = board[y_end + 1][x_end]
             if end == other_colour:
                 bottom = False

    #horizontal case:
    elif d_y == 0 and d_x == 1:
        coordinates = [y_end, x_end - length]
        if coordinates not in L:
            top = False
        else:
           beginning = board[y_end][x_end - length]
           if beginning == other_colour:
               top = False

        coordinates_of_end = [y_end, x_end + 1]
        if coordinates_of_end not in L:
            bottom = False
        else:
            end = board[y_end][x_end + 1]
            if end == other_colour:
                bottom = False

    #diagonal case:
    elif d_y == 1 and d_x == 1:
        coordinates = [y_end - length, x_end - length]
        if coordinates not in L:
            top = False
        else:
            beginning = board[y_end - length ][x_end - length]
            if beginning == other_colour:
                top = False

        coordinates_of_end = [y_end + 1, x_end + 1]
        if coordinates_of_end not in L:
            bottom = False
        else:
            end = board[y_end + 1][x_end + 1]
            if end == other_colour:
                bottom = False

    elif d_y == 1 and d_x == -1:
        coordinates = [y_end - length, x_end + length]
        if coordinates not in L:
            top = False

        else:
            beginning = board[y_end - length][x_end + length]
            if beginning == other_colour:
                top = False

        coordinates_of_end = [y_end + 1, x_end - 1]
        if coordinates_of_end not in L:
            bottom = False
        else:
            end = board[y_end + 1][x_end - 1]
            if end == other_colour:
                bottom = False

    if top == False and bottom == False:
        return "CLOSED"
    elif top == False and bottom == True:
        return "SEMIOPEN"
    elif top == True and bottom == False:
        return "SEMIOPEN"
    elif top == True and bottom == True:
        return "OPEN"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    string = ""
    count = 0
    count_of_open = 0
    count_of_semiopen = 0

    #vertical case
    if d_y == 1 and d_x == 0:
        for i in range(y_start, 8):
            if board[i][x_start] == col:
                count += 1
                last_coordinate = i

            elif board[i][x_start] != col:
                if count == length:
                    if is_bounded(board, last_coordinate, x_start, length, d_y, d_x) == "OPEN":
                        count_of_open += 1
                    elif is_bounded(board, last_coordinate, x_start, length, d_y, d_x) == "SEMIOPEN":
                        count_of_semiopen += 1

                count = 0

        if count == length:
            if is_bounded(board, last_coordinate, x_start, length, d_y, d_x) == "OPEN":
                count_of_open += 1
            elif is_bounded(board, last_coordinate, x_start, length, d_y, d_x) == "SEMIOPEN":
                    count_of_semiopen += 1

    #horizontal case
    elif d_y == 0 and d_x == 1:
        for i in range(8):
            if board[y_start][x_start + i] == col:
                count += 1
                last_coordinate = x_start + i

            elif board[y_start][x_start + i] != col:
                if count == length:
                    if is_bounded(board, y_start, last_coordinate, length, d_y, d_x) == "OPEN":
                        count_of_open += 1
                    elif is_bounded(board, y_start, last_coordinate, length, d_y, d_x) == "SEMIOPEN":
                        count_of_semiopen += 1

                count = 0

        if count == length:
            if is_bounded(board, y_start, last_coordinate, length, d_y, d_x) == "OPEN":
                count_of_open += 1
            elif is_bounded(board, y_start, last_coordinate, length, d_y, d_x) == "SEMIOPEN":
                count_of_semiopen += 1

    #diagonal case: HAVE TO WORK ON BECAUSE THE LOWER STARTING POINTS DONT WILL BE OUT OF BOUNDS
    elif d_y == 1 and d_x == 1:
        for i in range(8):
            if [y_start + i, x_start + i] in L:
                if board[y_start + i][x_start + i] == col:
                    count += 1
                    last_coordinate_y = y_start + i
                    last_coordinate_x = x_start + i

                elif board[y_start + i][x_start + i] != col:
                    if count == length:
                        if is_bounded(board, last_coordinate_y, last_coordinate_x, length, d_y, d_x) == "OPEN":
                            count_of_open += 1
                        elif is_bounded(board, last_coordinate_y, last_coordinate_x, length, d_y, d_x) == "SEMIOPEN":
                            count_of_semiopen += 1

                    count = 0

        if count == length:
            if is_bounded(board, last_coordinate_y, last_coordinate_x, length, d_y, d_x) == "OPEN":
                count_of_open += 1
            elif is_bounded(board, last_coordinate_y, last_coordinate_x, length, d_y, d_x) == "SEMIOPEN":
                count_of_semiopen += 1

            count = 0

    elif d_y == 1 and d_x == -1:

        for i in range(8):
            if [y_start + i, x_start - i] in L:
                if board[y_start + i][x_start - i] == col:
                    count += 1
                    last_coordinate_y = y_start + i
                    last_coordinate_x = x_start - i

                elif board[y_start + i][x_start - i] != col:
                    if count == length:
                        if is_bounded(board, last_coordinate_y, last_coordinate_x, length, d_y, d_x) == "OPEN":
                            count_of_open += 1
                        elif is_bounded(board, last_coordinate_y, last_coordinate_x, length, d_y, d_x) == "SEMIOPEN":
                            count_of_semiopen += 1

                    count = 0

        if count == length:
            if is_bounded(board, last_coordinate_y, last_coordinate_x, length, d_y, d_x) == "OPEN":
                count_of_open += 1
            elif is_bounded(board, last_coordinate_y, last_coordinate_x, length, d_y, d_x) == "SEMIOPEN":
                count_of_semiopen += 1

            count = 0



    return (count_of_open, count_of_semiopen)



def detect_rows(board, col, length):
    #would first check vertically
    open_seq_count = 0
    semi_open_seq_count = 0
    d_x = 0; d_y = 1

    for i in range(8):
        a, b = detect_row(board, col, 0, i, length, d_y, d_x)
        open_seq_count += a
        semi_open_seq_count += b


    #would check horizontally
    d_x = 1; d_y = 0
    for i in range(8):
        a, b = detect_row(board, col, i, 0, length, d_y, d_x)
        open_seq_count += a
        semi_open_seq_count += b


    #would check diagonally
    d_x = 1; d_y = 1
    for i in range(6):
        a, b = detect_row(board, col, i, 0, length, d_y, d_x)
        open_seq_count += a
        semi_open_seq_count += b


    d_x = -1; d_y = 1
    for i in range(6):
        a, b = detect_row(board, col, i, 7, length, d_y, d_x)
        open_seq_count += a
        semi_open_seq_count += b



    return open_seq_count, semi_open_seq_count

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def search_max(board):
    '''Creates a dictionary with the coordinates of (y,x) as the key and the score as the value, then find the first max value it encouters, and returns that coordinate
    '''
    #first it has to check if that space is open and create a list of open spaces
    H = []
    scores = {}
    for i in range(8):
        for k in range(8):
            if board[i][k] == " ":
                H.append((i, k))

    #then create a deep copy of the original board to run through the score function
    new_board = []
    for sublist in board:
        new_board.append(sublist[:])

    #then we get each tuple from the list H and insert a black for new_list, then run it into max score
    for i in range(len(H)):
        y, x = H[i]
        new_board[y][x] = "b"
        scores[H[i]] = score(new_board)
        new_board[y][x] = " "

    move_y, move_x = max(scores, key=scores.get)

    return (move_y, move_x)



def is_win(board):
    #for black
    u, t = detect_rows(board, "b", 5)
    if u != 0 or t != 0:
        return "Black won"

    #for white
    q, r = detect_rows(board, "w", 5)
    if q != 0 or r != 0:
        return "White won"

    list_of_board = []
    for i in range(8):
        for k in range(8):
           list_of_board.append(board[i][k])

    if " " not in list_of_board:
        return "Draw"

    else:
        return "Continue playing"



def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))






def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x



if __name__ == '__main__':
    board = [[' ', ' ', '', '', '', ' ', '', ' '], 
        ['', ' ', ' ', ' ', ' ', 'w', 'b', ' '], 
        ['', ' ', ' ', '', ' ', ' ', 'b', 'w'], 
        [' ', ' ', ' ', '', ' ', ' ', 'b', 'w'], 
        [' ', ' ', ' ', '', ' ', ' ', ' ', ' '], 
        ['', 'b', '', ' ', ' ', 'w', ' ', ' '], 
        ['b', ' ', ' ', '', '', 'w', 'b', 'b'], 
        ['b', ' ', ' ', '', '', 'w', 'b', ' ']]
    print_board(board)
    print(detect_rows(board, "b", 2))
