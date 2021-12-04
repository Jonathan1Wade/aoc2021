# Puzzle answers
a1 = 0
a2 = 0

with open('input.txt') as file:                                                     # open file
    A: list = [line.strip() for line in file]                                       # read file

nums = [int(i) for i in A[0].split(",")]                                            # read first line


def new_boards() -> list:                                                           # create new boards
    boards = []                                                                     # create empty list
    for i in A[1:]:                                                                 # for each line
        if i:                                                                       # if line is not empty
            boards[-1].append([[int(j.strip()), False] for j in i.split()])         # add new row
        else:                                                                       # if line is empty
            boards.append([])                                                       # add new board
    return boards                                                                   # return list of boards


def check_win(board: list) -> bool:                                                 # check if board is won
    for row in board:                                                               # for each row                                             
        if all([j[1] for j in row]):                                                # if all values are marked
            return True                                                             # return True

    for c in range(len(board[0])):                                                  # for each column                                      
        if all([j[1] for j in [r[c] for r in board]]):                              # if all values are marked
            return True                                                             # return True

    return False                                                                                    


def mark_num(board: list, num: int) -> list:                                        # mark number
    for row in board:                                                               # for each row
        for v in row:                                                               # for each value
            if v[0] == num:                                                         # if value is number             
                v[1] = True                                                         # mark value                        
    return board                                                                    # return board  


def score(board: list, num: int) -> int:                                            # score board     
    s = 0                                                                           # create score
    for row in board:                                                               # for each row
        for v in row:                                                               # for each value
            if not v[1]:                                                            # if value is not marked
                s += v[0]                                                           # add value to score
    return s * num                                                                  # return score


# Puzzle 1
boards1 = new_boards()                                                              # create new boards

for n in nums:                                                                      # for each number
    for b in range(len(boards1)):                                                   # for each board
        boards1[b] = mark_num(boards1[b], n)                                        # mark number
        if check_win(boards1[b]):                                                   # if board is won
            a1 = score(boards1[b], n)                                               # add score
            break                                                                   # break
    else:                                                                           # if board is not won
        continue                                                                    # continue
    break                                                                           # break


print(f"Puzzle 1 Answer:\n{a1}")