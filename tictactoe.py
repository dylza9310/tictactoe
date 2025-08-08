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
        print("Game restarted. New board:")
        main()
    else:
        print("Thanks for playing!")
        exit()

        
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
                continue
                
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

        if board.count("x") + board.count("o") >= 8:
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

        if board.count("x") + board.count("o") >= 8:
            print("Game Over. It's a draw!")
            restart_game()
            return

def minimax(board, depth, is_maximizing):
    #Check if the game is over
    if check_win():
        return 1 if is_maximizing else -1
    if board.count('') == 0:
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9): # Loop through all possible moves
            if board[i] == '': # If the position is empty
                board[i] = 'o' 
                score = minimax(board, depth + 1, False) # Evaluate the move
                board[i] = ''
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('+inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'x'
                score = minimax(board, depth + 1, True)
                board[i] = ''
                best_score = min(score, best_score)
        return best_score

def human_vs_hardcomputer():
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
            
        print("Hard Computer's turn...")
        # Hard computer uses minimax algorithm
        best_score = float('-inf') # Initialize best score
        best_move = None 
        
        for i in range(9): # Loop through all possible moves
            if board[i] == '': # If the position is empty
                board[i] = 'o' # Make the move
                score = minimax(board, 0, False) # Evaluate the move
                board[i] = '' # Undo the move
                if score > best_score:  # If this move is better than the best found so far
                    best_score = score # Update the best score
                    best_move = i  # Update the best move
        if best_move is not None:
            board[best_move] = 'o'
            print(f"Hard Computer chose position {best_move}")
            print(board)
            if check_win():
                print("Hard Computer wins!")
                restart_game()
                return

        if board.count("x") + board.count("o") >= 8:
            print("Game Over. It's a draw!")
            restart_game()
            return

def main(): 
    str(print("Welcome to Tic Tac Toe!"))
    str(print("Choose game mode: '1' for 2 Players, '2' for Easy AI, '3' for Intermediate AI, '4' for Hard AI"))
    game_mode = input("Enter 1, 2, 3 or 4: ")
    if game_mode == '1':
        human_vs_human()
    elif game_mode == '2':
        human_vs_easycomputer()
    elif game_mode == '3':
        human_vs_intermediatecomputer()
    elif game_mode == '4':
        human_vs_hardcomputer()
    else:
        print("Invalid choice. Please restart the game and choose a valid mode.")
        main()  # Restart the game after it ends

board = ['', '', '', '', '', '', '', '', '']
main()
