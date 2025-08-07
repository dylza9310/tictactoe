board = ['', '', '', '', '', '', '', '', '']

while board.count("x") < 9:
    x = int(input("Player 1 pick a position (0-8): "))
    if board[x] == '':
        board[x] = 'x'
        print(board)
    else:
        print("Position already taken. Try again.")

print(board)