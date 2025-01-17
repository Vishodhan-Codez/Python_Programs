import random
import time

def squares(b):  # Tic Tac Toe board
    print(f'''
 {b[0]} | {b[1]} | {b[2]} 
---|---|---
 {b[3]} | {b[4]} | {b[5]} 
---|---|---
 {b[6]} | {b[7]} | {b[8]} 
''')

def winner(b, p):  # player has a w ?
    wc = [  # winning combos
        (0, 4, 8), (0, 3, 6), (0, 1, 2),
        (1, 4, 7), (2, 4, 6), (2, 5, 8),
        (3, 4, 5), (6, 7, 8)
    ]
    return any(b[x] == b[y] == b[z] == p for x, y, z in wc)

def ai_move(b, ai, h):  # AI strategy
    for i in range(9):  # w AI move 
        if b[i] == " ":
            b[i] = ai  # placeholder for AI 
            if winner(b, ai):  # w moves for AI
                time.sleep(random.uniform(0.256, 2.864))  # fool the player
                return i
            b[i] = " "  # reset
    for i in range(9):  # block human w move
        if b[i] == " ":
            b[i] = h  # placeholder for AI
            if winner(b, h):  # block w human move
                b[i] = " "
                time.sleep(random.uniform(0.256, 2.864))  # fool the player
                return i
            b[i] = " "  # reset
    # no w or l move , random
    return random.choice([i for i, x in enumerate(b) if x == " "])

def tic_tac_toe():  # The main function to play the game
    while True:
        print("\n1. Human vs Human\n2. Human vs AI")  # gamemode
        m = input("Mode (1/2): ")  # input
        while m not in "12":  
            m = input("Invalid! Choose 1 or 2: ")
        
        b, cp = [" "] * 9, "X"  # make the board
        if m == "2":  # Human vs AI mode
            h = input("Play as X or O? ").upper()  # choice
            while h not in "XO":  
                h = input("Invalid! Choose X or O: ").upper()
            ai = "O" if h == "X" else "X"  # ai symbol assign

        squares([i for i in range(9)])  # show board position
        
        for _ in range(9): 
            if m == "1" or (m == "2" and cp == h):  
                while True:
                    try:
                        mv = int(input(f"Player {cp}, choose (0-8): "))  
                        if mv not in range(9) or b[mv] != " ":  
                            raise ValueError
                        break
                    except:  
                        print("Invalid move! Choose a valid position.")
            else:  # AI's turn
                print(f"AI ({ai}) is thinking...")
                mv = ai_move(b, ai, h) 
            
            b[mv] = cp  # place symbol
            cp = "O" if cp == "X" else "X"  
            squares(b)  
            
            if winner(b, b[mv]):  
                print(f"{'AI' if m == '2' and cp != h else 'Player'} {b[mv]} wins!")
                break
        else:
            print("Draw!")
        if input("Play again? (y/n): ").lower() != "y":
            break

tic_tac_toe()
