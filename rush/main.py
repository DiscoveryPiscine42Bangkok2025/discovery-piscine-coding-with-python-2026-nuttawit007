#!/usr/bin/env python3
from checkmate import checkmate

""" Test cases 1 """
def main():
    board = """\
R...
.K..
..P.
....\
""" 
    print(board)
    board = board.strip().splitlines()
    checkmate(board)

""" Test cases 2 """
# def main():
#     board = """\
# R...
# .K.....
# ..P.
# ....\
# """ 
#     print(board)
#     board = board.strip().splitlines()
#     checkmate(board)

""" Test cases 3 """
# def main():
#     board = """\
# R...
# .K..
# ..K.
# ....\
# """ 
#     print(board)
#     board = board.strip().splitlines()

""" Test cases 4 """
# def main():
#     board = """\
# R...
# ....
# ..P.
# ....\
# """ 
#     print(board)
#     board = board.strip().splitlines()
#     checkmate(board)

""" Test cases 5 """
# def main():
#     board = """\
# R...
# .K..
# ..K.
# ....\
# """ 
#     print(board)
#     board = board.strip().splitlines()
#     checkmate(board)

""" Test cases 6 """
# def main():
#     board = """\
# ...Q
# .K..
# ...B
# P...\
# """ 
#     print(board)
#     board = board.strip().splitlines()
#     checkmate(board)

main()
#test with ./main.py | cat -e