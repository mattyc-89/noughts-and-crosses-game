def draw_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print("\n")
        
def is_valid_move(board, row, col):
    # check if the row and column are within bounds
    if row < 0 or row >= 3 or col < 0 or col >= 3:
        return False
    # check if the cell is already occupied
    if board[row][col] != " ":
        return False
    return True

def make_move(board, row, col, player):
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False

def check_winner(board):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column separated by a space): ")
            row, col = map(int, move.split())
            return row - 1, col - 1  # convert to 0-indexed
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
        except IndexError:
            print("Invalid move. Please enter numbers between 1 and 3 for both row and column.")

def play_game():
    board = [[" " ] *3 for _ in range(3)]
    current_player = "X"
    
    while True:
        draw_board(board)
        row, col = get_player_move(current_player)
        
        if make_move(board, row, col, current_player):
            winner = check_winner(board)
            if winner:
                draw_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_draw(board):
                draw_board(board)
                print("The game is a draw!")
                break
            
            # switch players
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")


def main():
    print("Welcome to Coomber's Noughts and Crosses Game")
    play_game()
    

if __name__ == "__main__":
    main()