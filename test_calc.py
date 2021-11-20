arr = [[" "," "," "],[" ","b"," "]]

def is_empty(board):
    for i in board:
        if "b" in i or "w" in i:
            return False
    return True

print(is_empty(arr))