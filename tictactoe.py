board = ['', '', '', '', '', '', '', '', '']

while board.count("x") + board.count("o") < 9:
    x = int(input("Player 1 pick a position (0-8): "))
    if board[x] == '' or board[y] == '':
        board[x] = 'x'
        print(board)
    else:
        print("Position already taken. Try again.")

    y = int(input("Player 2 pick a position (0-8): "))
    if board[x] == '' or board[y] == '':
        board[y] = 'o'
        print(board)
    else:
        print("Position already taken. Try again.")

    if board.count("x") + board.count("o") >= 9:
        print("Game Over. It's a draw!")
        break
    

print(board)