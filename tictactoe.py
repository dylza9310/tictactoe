board = ['', '', '', '', '', '', '', '', '']

def check_win():
    """Check if there is a winner."""
    # Define the winning conditions
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
        
def human_vs_human():
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


def human_vs_easycomputer():
    import random
    while board.count("x") + board.count("o") < 9:
        x = int(input("Player pick a position (0-8): "))
        if board[x] == '':
            board[x] = 'x'
            print(board)
            if check_win():
                print("Player 1 wins!")
                restart_game()
                return
        else:
            print("Position already taken. Try again.")
            continue

        print("Computer's turn...")
        # Computer picks a random empty spot
        empty_spots = [i for i, v in enumerate(board) if v == '']
        if not empty_spots:
            break
        y = random.choice(empty_spots)
        board[y] = 'o'
        print(f"Computer chose position {y}")
        print(board)
        if check_win():
            print("Computer wins!")
            restart_game()
            return

        if board.count("x") + board.count("o") >= 9:
            print("Game Over. It's a draw!")
            restart_game()
            return

def human_vs_intermediatecomputer():
    import random
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    while board.count("x") + board.count("o") < 9:
        x = int(input("Player pick a position (0-8): "))
        if board[x] == '':
            board[x] = 'x'
            print(board)
            if check_win():
                print("Player wins!")
                restart_game()
                return
        else:
            print("Position already taken. Try again.")
            continue

        print("Intermediate Computer's turn...")
        # Placeholder for intermediate computer logic
        # 
        blocked = False
        for condition in win_conditions:
            if all(board[i] == 'o' for i in condition if board[i] != '') and any(board[i] == '' for i in condition):
                y = next(i for i in condition if board[i] == '')
                board[y] = 'o'
                blocked = True
                print(f"Intermediate Computer chose position {y}")
                break
        if not blocked:
            y = random.choice([i for i, v in enumerate(board) if v == ''])
            board[y] = 'o'
            print(f"Intermediate Computer chose position {y}")
            print(board)
        if check_win():
            print("Intermediate Computer wins!")
            restart_game()
            return

        if board.count("x") + board.count("o") >= 9:
            print("Game Over. It's a draw!")
            restart_game()
            return

str(print("Welcome to Tic Tac Toe!"))
str(print("Choose game mode: 1 for Human vs Human, 2 for Human vs Easy Computer, 3 for Human vs Intermediate Computer"))
game_mode = input("Enter 1, 2 or 3: ")
if game_mode == '1':
    human_vs_human()
elif game_mode == '2':
    human_vs_easycomputer()
elif game_mode == '3':
    human_vs_intermediatecomputer()
else:
    print("Invalid choice. Please restart the game and choose a valid mode.")
    exit()