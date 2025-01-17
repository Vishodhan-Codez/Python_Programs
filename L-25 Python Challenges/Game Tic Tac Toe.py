import random
import time

def squares(board):  # Tic Tac Toe board
    print(f'''
 {board[0]} | {board[1]} | {board[2]} 
---|---|---
 {board[3]} | {board[4]} | {board[5]} 
---|---|---
 {board[6]} | {board[7]} | {board[8]} 
''')

def winner(board, player):  # player has a win?
    win_combos = [  # winning combos
        (0, 4, 8), (0, 3, 6), (0, 1, 2),
        (1, 4, 7), (2, 4, 6), (2, 5, 8),
        (3, 4, 5), (6, 7, 8)
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combos)

def ai_move(board, ai, human):  # AI strategy
    for i in range(9):  # AI winning move
        if board[i] == " ":
            board[i] = ai  # placeholder for AI 
            if winner(board, ai):  # winning move for AI
                time.sleep(random.uniform(0.256, 2.864))  # fool the player
                return i
            board[i] = " "  # reset
    for i in range(9):  # block human winning move
        if board[i] == " ":
            board[i] = human  # placeholder for AI
            if winner(board, human):  # block human winning move
                board[i] = " "
                time.sleep(random.uniform(0.256, 2.864))  # fool the player
                return i
            board[i] = " "  # reset
    # no winning or blocking move, choose randomly
    return random.choice([i for i in range(9) if board[i] == " "])

def tic_tac_toe():  # mc
    print("Hello ! This is a game of Tic Tac Toe")
    print("Just in case you don't know the rules -\nIt's three of your symbols in any row/column/diagonal to win\nYou place one symbol per turn until all the squares are filled\n\nLet the games begin !!")
    
    while True:
        print("\n1. Human vs Human\n2. Human vs AI")  # game mode
        mode = input("Mode (1/2): ")  # input
        while mode not in "12":  
            mode = input("Invalid! Choose 1 or 2: ")
        
        board, current_player = [" "] * 9, "X"  # initialize the board
        if mode == "2":  # Human vs AI mode
            human = input("Play as X or O? ").capitalize() # choice
            while human not in "XOxo":  
                human = input("Invalid! Choose X or O: ")
            ai = "O" if human == "X" else "X"  # AI symbol assignment

        squares([i for i in range(9)])  # show board position
        
        for _ in range(9): 
            if mode == "1" or (mode == "2" and current_player == human):  
                while True:
                    try:
                        move = int(input(f"Player {current_player}, choose (0-8): "))  
                        if move not in range(9) or board[move] != " ":  
                            raise ValueError
                        break
                    except:  
                        print("Invalid move! Choose a valid position.")
            else:  # AI's turn
                print(f"AI ({ai}) is thinking...")
                move = ai_move(board, ai, human) 
            
            board[move] = current_player  # place symbol
            current_player = "O" if current_player == "X" else "X"  
            squares(board)  
            
            if winner(board, board[move]):  
                print(f"{board[move]} wins!")
                break
        else:
            print("Draw!")
        
        if input("Play again? (y/n): ").lower() != "y":
            break

tic_tac_toe()
