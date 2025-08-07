board = ['', '', '', '', '', '', '', '', '']

while board.count("x") + board.count("o") < 9:
    x = int(input("Player 1 pick a position (0-8): "))
    y = int(input("Player 2 pick a position (0-8): "))
    if board[x] == '' or board[y] == '':
        board[x] = 'x'
        board[y] = 'o'
        print(board)
    if board.count("x") + board.count("o") >= 9:
        print("Game Over. It's a draw!")
        break
    else:
        print("Position already taken. Try again.")

print(board)