# BEGIN Tic Tac Toe Game (2 Players)


#     SETUP
#     - Create the board as 9 spaces numbered 1 through 9 like this:
#         1 | 2 | 3
#         ---------
#         4 | 5 | 6
#         ---------
#         7 | 8 | 9
   
#     - User uses "X", Computer uses "O"
#     User goes first
#     - Ask both players for their names (to save winner scores later)
#     - Keep track of how many moves have been made (stops at 9 for a tie)


#     # GAMEPLAY
#     - Show the current board after every move
#     - Ask current player which number position they want to place their mark
#     - Check if that position is empty (not already taken by X or O)
#     - If it's taken, make them choose again
#     - If it's empty, put their mark there and add 1 to move count


#     # CHECKING FOR WINNER (after every move)
#     - After each move, check if current player has 3 in a row:
#         * Horizontal rows: positions (1,2,3) or (4,5,6) or (7,8,9)
#         * Vertical columns: positions (1,4,7) or (2,5,8) or (3,6,9)
#         * Diagonal lines: positions (1,5,9) or (3,5,7)
   
#     - If they have 3 in a row, they win!
#     - If all 9 moves are made and no winner, it's a tie


#      END OF GAME
#     - If someone wins:
#         * Show the final board
#         * Announce the winner
#           Return the number of turns (score)
   
#     - If tie:
#         * Show final board
#         * Announce it's a tie
        #   Return False
#     # SAMPLE OUTPUT
   
#     1 | 2 | 3
#     ---------
#     4 | 5 | 6
#     ---------
#     7 | 8 | 9
   
#     Player X choose position (1-9): 5
   
#     1 | 2 | 3
#     ---------
#     4 | X | 6
#     ---------
#     7 | 8 | 9
   
#     Player O choose position (1-9): 1
   
#     O | 2 | 3
#     ---------
#     4 | X | 6
#     ---------
#     7 | 8 | 9
   
#     (game continues until someone wins or tie)


# END
def tic_tac():
   import json
   import random
   # SETUP
   print("Welcome to Tic Tac Toe!")
   player1_name = "You"
   # Create the board (1-9 positions)
   board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
   
   # Keep track of moves
   moves = 0
   current_player = "X"
   current_name = player1_name
   player2_name = 'opponent'
   # Function to show the board
   def show_board():
       print("\n" + board[0] + " | " + board[1] + " | " + board[2])
       print("---------")
       print(board[3] + " | " + board[4] + " | " + board[5])
       print("---------")
       print(board[6] + " | " + board[7] + " | " + board[8])
       print("")
   
   # Function to check for winner
   def check_winner():
       # All winning combinations
       win_combos = [
           [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
           [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
           [0, 4, 8], [2, 4, 6]              # diagonals
       ]
       
       for combo in win_combos:
           if board[combo[0]] == board[combo[1]] == board[combo[2]]:
               return True
       return False
   
   # Show empty board at start
   show_board()
   
   # GAMEPLAY
   while moves < 9:
       # Ask current player for their move
       print(current_name + " (" + current_player + "), choose position (1-9): ", end="")
       position = int(input())
       
       # Convert to list index (1-9 to 0-8)
       index = position - 1
       
       # Check if position is valid and empty
       if index < 0 or index > 8:
           print("Invalid position! Choose 1-9.")
           continue
       
       if board[index] == "X" or board[index] == "O":
           print("That spot is taken! Choose another.")
           continue
       
       # Place the mark
       board[index] = current_player
       moves = moves + 1
       
       # Show updated board
       show_board()
       
       # Check for winner
       if check_winner():
           # END OF GAME - WINNER
           print(current_name + " wins! They took " + str(moves) + " moves. This is your score!")
           
           break
       
       # Switch players
       if current_player == "X":
           current_player = "O"
           current_name = player2_name
       else:
           current_player = "X"
           current_name = player1_name
   
   # Check for tie game
   if moves == 9 and not check_winner():
       # END OF GAME - TIE
       print("It's a tie!")



