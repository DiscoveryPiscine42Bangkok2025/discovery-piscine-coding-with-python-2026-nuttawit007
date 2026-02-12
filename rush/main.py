#!/usr/bin/env python3
from checkmate import checkmate

# def main():
#     board = """\
# R...
# .K..
# ..P.
# ....\
# """ 
#     print(board)

# def main():
#     board = """\
# ..
# .K\
# """

def main():
    board = """\
...Q
.K..
..B.
P...\
""" 
    print(board)

    board = board.strip().splitlines()
    checkmate(board)

main()
#test with python3 main.py | cat -e