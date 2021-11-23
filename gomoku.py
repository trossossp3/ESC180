"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 30, 2021
"""

def is_empty(board):
    for i in board:
        if "b" in list or "w" in list:
            return False
    return True

    
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    bounded = 0
    if d_y == 0 and d_x == 1:
        y_init = y_end
        x_init = x_end -(length-1)
        if(x_init == 0): bounded+=1
        else:
            if(board[y_end][x_init-1] != " "): bounded+=1 #if stone beside bounded increases
        if(x_end == len(board)): bounded+=1 #if the stone is at the end or begining it must atleast be semi bounded
        else: 
            if(board[y_end][x_end+1]!=" "): bounded+=1

    elif d_y ==1 and d_x == 0:
        x_init = x_end
        y_init = y_end -(length-1)
        if(y_init == 0): bounded+=1
        else:
            if(board[y_init-1][x_init] != " "): bounded+=1 #if stone beside bounded increases
        if(y_end == len(board)): bounded+=1 #if the stone is at the end or begining it must atleast be semi bounded
        else: 
            if(board[y_end+1][x_init]!=" "): bounded+=1        
    elif d_y ==1 and d_x ==1:
        y_init = y_end - (length-1)
        x_init = x_end + (length-1) #since starting from right x will be greater up board
        if(x_init == 0 or y_init == 0): bounded+=1
        else:
            if(board[y_init-1][x_init+1] != " "): bounded+=1 #if stone right diagonal
        if(x_end == len(board) or y_end == len(board)): bounded+=1 #if the stone is at the end or begining it must atleast be semi bounded
        else: 
            if(board[y_end+1][x_end+1]!=" "): bounded+=1 #if stone at end increase bounded
    else: #up right to low left
        y_init = y_end - (length-1)
        x_init = x_end -(length-1)
        if(x_init == len(board) or y_init == 0): bounded+=1 #bounded if at top or right side to 
        else:
            if(board[y_init-1][x_init+1] != " "): bounded+=1 #if stone beside bounded increases
        if(x_end == 0 or y_end == len(board)): bounded+=1 #if the stone is at the end or begining it must atleast be semi bounded
        else: 
            if(board[y_end+1][x_end-1]!=" "): bounded+=1 #if stone at end increase bounded

    if(bounded ==1):
        return "SEMIOPEN"
    elif(bounded ==2): return "CLOSED"
    else: return "OPEN"

    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    len_counter = 0
    open_seq_count, semi_open_seq_count = 0,0
    on_streak = False

    if(d_y == 0 and d_x ==1):
        y = y_start
        init=[]
        for x in range(x_start, len(board[0])):
            if board[y][x] == col:
                if not on_streak:
                    init = [y,x] #if this is the first col that is in the streak it is the init cootd
                len_counter+=1
                on_streak = True
            else:
                if on_streak: # this would run when u were on a streak but now u are not on a streak
                    on_streak = False
                    
                    if len_counter>=length:
                        bounded = is_bounded(board,y,x,len_counter,d_y,d_x)
                        if bounded == "OPEN":
                            open_seq_count+=1
                        elif bounded == "SEMIOPEN":
                            semi_open_seq_count+=1
                len_counter = 0


    if(d_y == 1 and d_x ==0):
        x = x_start
        init=[]
        for y in range(y_start, len(board)):
            if board[y][x] == col:
                if not on_streak:
                    init = [y,x] #if this is the first col that is in the streak it is the init cootd
                len_counter+=1
                on_streak = True
            else:
                if on_streak: # this would run when u were on a streak but now u are not on a streak
                    on_streak = False
                    
                    if len_counter>=length:
                        bounded = is_bounded(board,y,x,len_counter,d_y,d_x)
                        if bounded == "OPEN":
                            open_seq_count+=1
                        elif bounded == "SEMIOPEN":
                            semi_open_seq_count+=1
                len_counter = 0
    if(d_y == 1 and d_x ==0):
        x = x_start
        init=[]
        for y in range(y_start, len(board)):
            if board[y][x] == col:
                if not on_streak:
                    init = [y,x] #if this is the first col that is in the streak it is the init cootd
                len_counter+=1
                on_streak = True
            else:
                if on_streak: # this would run when u were on a streak but now u are not on a streak
                    on_streak = False
                    
                    if len_counter>=length:
                        bounded = is_bounded(board,y,x,len_counter,d_y,d_x)
                        if bounded == "OPEN":
                            open_seq_count+=1
                        elif bounded == "SEMIOPEN":
                            semi_open_seq_count+=1
                len_counter = 0
    if(d_y == 1 and d_x ==0):
        x = x_start
        y= y_start
        init=[]
        while x <= len(board) and y<= len(board):
            if board[y][x] == col:
                if not on_streak:
                    init = [y,x] #if this is the first col that is in the streak it is the init cootd
                len_counter+=1
                on_streak = True
            else:
                if on_streak: # this would run when u were on a streak but now u are not on a streak
                    on_streak = False
                    
                    if len_counter>=length:
                        bounded = is_bounded(board,y,x,len_counter,d_y,d_x)
                        if bounded == "OPEN":
                            open_seq_count+=1
                        elif bounded == "SEMIOPEN":
                            semi_open_seq_count+=1
                len_counter = 0
            x+=1 #since we are doing diagonal must add one to x
            y+=1    
    if(d_y == 1 and d_x ==0):
        x = x_start
        y= y_start
        init=[]
        while x >= len(board) and y<= len(board):
            if board[y][x] == col:
                if not on_streak:
                    init = [y,x] #if this is the first col that is in the streak it is the init cootd
                len_counter+=1
                on_streak = True
            else:
                if on_streak: # this would run when u were on a streak but now u are not on a streak
                    on_streak = False
                    
                    if len_counter>=length:
                        bounded = is_bounded(board,y,x,len_counter,d_y,d_x)
                        if bounded == "OPEN":
                            open_seq_count+=1
                        elif bounded == "SEMIOPEN":
                            semi_open_seq_count+=1
                len_counter = 0
            x-=1 #since we are doing diagonal must add one to x
            y+=1    
    return open_seq_count, semi_open_seq_count
    
def detect_rows(board, col, length):
    ####CHANGE ME
    open_seq_count, semi_open_seq_count = 0, 0
    
    # (0,1) direction first
    for y in len(board):
        open_seq_count += detect_row(board,col,y,0,length,0,1)[0]
        semi_open_seq_count +=(board,col,y,0,length,0,1)[1]
    #go col by col and look down (1,0)
    for x in len(board):
        open_seq_count += detect_row(board,col,0,x,length,1,0)[0]
        semi_open_seq_count +=(board,col,0,x,length,1,0)[1]
    #diagonal left and down check all the rows starting bottom left going top right
    for y in len(board):
        open_seq_count += detect_row(board,col,y,0,length,1,1)[0]
        semi_open_seq_count +=(board,col,y,0,length,1,1)[1]
    for x in len(board):
        open_seq_count += detect_row(board,col,0,x,length,1,1)[0]
        semi_open_seq_count +=(board,col,0,x,length,1,1)[1]
     #diagonal right and down check all the rows starting bottom right going top right
    for y in len(board):
        open_seq_count += detect_row(board,col,y,0,length,1,-1)[0]
        semi_open_seq_count +=(board,col,y,0,length,1,-1)[1]
    #check paramameters
    #check paramameters
    #check paramameters
    for x in range(len(board), 0, -1): #check parameters
        open_seq_count += detect_row(board,col,0,x,length,1,1)[0]
        semi_open_seq_count +=(board,col,0,x,length,1,1)[1]
    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    copy_board = board.copy()
    
    return move_y, move_x
    

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

    
def is_win(board):
    pass


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


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    play_gomoku(8)
    
