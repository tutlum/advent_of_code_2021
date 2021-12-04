import sys
#import numpy as np

''' read file name and outputs an numpy array '''
def readfile(filen, includeblanks=False):
    f=open(filen,"r")
    content = f.read()
    m = [x for x in content.split("\n") if includeblanks or x!=""]
    f.close()
    return m

'''
in: list of inputs:
 numberlist

 5x5

 5x5

 ...
'''
def format_data(l):
    numbers=[int(x.strip()) for x in l[0].split(",")]
    boardlist=[]
    board=[]
    for bl in l[2:]:
        if bl=="":
            boardlist.append(board)
            board=[]
        else: board.append([int(x.strip()) for x in bl.split(" ") if x!=""])
    boardlist.append(board)
    return numbers, boardlist

def solution(filen):
    m=readfile(filen, True)
    n,b=format_data(m)
    print("Read following board sizes: ", len(b), len(b[0]), len(b[0][0]), " and these numbers: ", n)
    marker=build_markers(len(b), len(b[0]))
    num, fwb = solution1(marker, b, n)
    print(num, "board:", fwb, calc_score(marker[fwb], b[fwb], num))

    marker=build_markers(len(b), len(b[0]))
    num, lwb = solution2(marker, b, n)
    print(num, "board:", lwb, calc_score(marker[lwb], b[lwb], num))

def solution1(marker, b, n):
    for number in n:
        for i in range(len(b)):
            mark_board(number, b[i], marker[i])
            if check_bingo(marker[i]):
                return number, i

def solution2(marker, b, n):
    board_wins=list(range(len(b)))
    for number in n:
        removers=[]
        for i in board_wins:
            mark_board(number, b[i], marker[i])
            if check_bingo(marker[i]):
                removers.append(i)
                if len(board_wins)-len(removers)==0:
                    return number, i
        for r in removers: board_wins.remove(r)

def print_m(m):
    print( "\n".join([" ".join([str(i) for i in x]) for x in m]))

def calc_score(marker, board, number):
    size=len(board)
    summe=0
    for i in range(size):
        for j in range(size):
            if marker[i][j]==0: summe+=board[i][j]
    return summe*number

def build_markers(anz, size):
    return [[[0 for x in range(size)] for y in range(size)] for z in range(anz)]

def mark_board(number, board, marker):
    size=len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j]==number: marker[i][j]=1

def check_bingo(marker, diag=False):
    size=len(marker)
    for i in range(size):
        if sum(marker[i])==5:
            #print("row", i)
            return True
        if sum([marker[j][i] for j in range(size)])==5:
            #print("col", i)
            return True
    if diag:
        if sum([marker[j][j] for j in range(size)])==5:
            #print("diag", i)
            return True
        if sum([marker[size-1-j][j] for j in range(size)])==5:
            #print("anti diag", i)
            return True
    return False
    


'''
converts a binary number to a decimal
'''
def bin_to_dec(bin_num):
    return int("".join([str(x) for x in bin_num]),2)

if __name__ == '__main__':
    if len(sys.argv)>1:
        solution(sys.argv[1])
    else: solution("input1.txt")
