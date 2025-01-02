def print_board(board):
    for row in board:
        print(" ".join(row))
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn:")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = players[current_player]
            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = 1 - current_player
        else:
            print("Invalid move. Try again.")
tic_tac_toe()
