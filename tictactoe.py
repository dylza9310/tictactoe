board = {'0': '', '1': '', '2': '',
         '3': '', '4': '', '5': '',
         '6': '', '7': '', '8': ''}

def board_display(board):
    print('-+-+-')
    print(board['0'] + '|' + board['1'] + '|' + board['2'])
    print('-+-+-')
    print(board['3'] + '|' + board['4'] + '|' + board['5'])
    print('-+-+-')
    print(board['6'] + '|' + board['7'] + '|' + board['8'])
    print('-+-+-')


def check_win(board):
    """Check if there is a winner."""
    win_conditions = [
        ['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8'],
        ['0', '3', '6'], ['1', '4', '7'], ['2', '5', '8'],
        ['0', '4', '8'], ['2', '4', '6']
    ]
    for condition in win_conditions:
        if all(board[pos] == 'x' for pos in condition):
            return True
        if all(board[pos] == 'o' for pos in condition):
            return True
    return False

def restart_game():
    print("Do you want to restart the game? (yes/no):")
    if input().lower() == 'yes':
        global board
        board = {'0': '', '1': '', '2': '',
                 '3': '', '4': '', '5': '',
                 '6': '', '7': '', '8': ''}
        print("Game restarted. New board:")
        main()
    else:
        print("Thanks for playing!")
        exit()

def human_vs_human():
    while sum(1 for val in board.values() if val) < 9:
        x = input("Player 1 pick a position (0-8): ")
        if board[x] == '':
            board[x] = 'x'
            if check_win(board):
                board_display(board)
                print("Player 1 wins!")
                restart_game()
                return
        else:
            print("Position already taken. Try again.")
            continue

        y = input("Player 2 pick a position (0-8): ")
        if board[y] == '':
            board[y] = 'o'
            if check_win(board):
                board_display(board)
                print("Player 2 wins!")
                restart_game()
                return
        else:
            print("Position already taken. Try again.")

        if sum(1 for val in board.values() if val) >= 9:
            board_display(board)
            print("Game Over. It's a draw!")
            restart_game()
            return

def human_vs_easycomputer():
    import random
    while sum(1 for val in board.values() if val) < 9:
        x = input("Player pick a position (0-8): ")
        if board[x] == '':
            board[x] = 'x'
            if check_win(board):
                board_display(board)
                print("Player wins!")
                restart_game()
                return
        else:
            print("Position already taken. Try again.")
            continue

        print("Computer's turn...")
        empty_spots = [pos for pos, val in board.items() if val == '']
        if not empty_spots:
            break
        y = random.choice(empty_spots)
        board[y] = 'o'
        print(f"Computer chose position {y}")
        board_display(board)
        if check_win(board):
            print("Computer wins!")
            restart_game()
            return

        if sum(1 for val in board.values() if val) >= 9:
            print("Game Over. It's a draw!")
            restart_game()
            return

def human_vs_intermediatecomputer():
    import random
    win_conditions = [
        ['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8'],
        ['0', '3', '6'], ['1', '4', '7'], ['2', '5', '8'],
        ['0', '4', '8'], ['2', '4', '6']
    ]
    while sum(1 for val in board.values() if val) < 9:
        x = input("Player pick a position (0-8): ")
        if board[x] == '':
            board[x] = 'x'
            if check_win(board):
                board_display(board)
                print("Player wins!")
                restart_game()
                return
        else:
            print("Position already taken. Try again.")
            continue

        print("Intermediate Computer's turn...")
        blocked = False
        for condition in win_conditions:
            if all(board[pos] == 'o' for pos in condition if board[pos] != '') and any(board[pos] == '' for pos in condition):
                y = next(pos for pos in condition if board[pos] == '')
                board[y] = 'o'
                blocked = True
                print(f"Intermediate Computer chose position {y}")
                break
        if not blocked:
            empty_spots = [pos for pos, val in board.items() if val == '']
            y = random.choice(empty_spots)
            board[y] = 'o'
            print(f"Intermediate Computer chose position {y}")
        board_display(board)
        if check_win(board):
            print("Intermediate Computer wins!")
            restart_game()
            return

        if sum(1 for val in board.values() if val) >= 9:
            print("Game Over. It's a draw!")
            restart_game()
            return

def main():
    print("Welcome to Tic Tac Toe!")
    print("Choose game mode: '1' for 2 Players, '2' for Easy AI, '3' for Intermediate AI, '4' for Hard AI")
    game_mode = input("Enter 1, 2, 3 or 4: ")
    if game_mode == '1':
        human_vs_human()
    elif game_mode == '2':
        human_vs_easycomputer()
    elif game_mode == '3':
        human_vs_intermediatecomputer()
    elif game_mode == '4':
        print("Hard mode is not implemented yet. Please choose another mode.")
        main()
    else:
        print("Invalid choice. Please restart the game and choose a valid mode.")
        main()

main()

