board = ['', '', '', '', '', '', '', '', '']

def check_win():
    if board[x] or board[y]:
        win_conditions = [0, 1, 2], [3, 4, 5], [6, 7, 8], \
                        [0, 3, 6], [1, 4, 7], [2, 5, 8], \
                        [0, 4, 8], [2, 4, 6]
    return True if any(all(board[i] == 'x' for i in condition) for condition in win_conditions) or \
                   any(all(board[i] == 'o' for i in condition) for condition in win_conditions) else False

def restart_game():
    print("Do you want to restart the game? (yes/no):")
    if input().lower() != 'no':
        global board
        board = ['', '', '', '', '', '', '', '', '']
        print("Game restarted. New board:", board)
    else:
        print("Thanks for playing!")

while board.count("x") + board.count("o") < 9:
    x = int(input("Player 1 pick a position (0-8): "))
    if board[x] == '' or board[y] == '':
        board[x] = 'x'
        print(board)
        if check_win():
            print("Player 1 wins!")
            restart_game()
    else:
        print("Position already taken. Try again.")
        

    y = int(input("Player 2 pick a position (0-8): "))
    if board[x] == '' or board[y] == '':
        board[y] = 'o'
        print(board)
        if check_win():
            print("Player 2 wins!")
            restart_game()
    else:
        print("Position already taken. Try again.")

    if board.count("x") + board.count("o") >= 8:
        print("Game Over. It's a draw!")
        restart_game()


print(board)