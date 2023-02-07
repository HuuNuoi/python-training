# Trò chơi cờ vua bằng python

board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def print_board(board):
    for row in board:
        print(' '.join(row))


def move(board, turn, x, y):
    if board[x-1][y-1] == '_':
        board[x-1][y-1] = turn
        return board
    else:
        print("Vị trí này đã được đánh, hãy chọn vị trí khác")
        return False


def check_win(board, turn):
    for row in board:
        if row.count(turn) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == turn:
            return True
    if board[0][0] == board[1][1] == board[2][2] == turn:
        return True
    if board[2][0] == board[1][1] == board[0][2] == turn:
        return True
    return False


player1 = 'X'
player2 = 'O'
turn = player1


def game():
    win = False
    while not win:
        print_board(board)
        x = int(
            input(f'Lượt đi của {turn}, bạn hãy chọn ô nào (từ 1 đến 9): '))
        y = int(input('Nhập hàng: '))
        move(board, turn, x, y)
        if check_win(board, turn):
            print(f'{turn} thắng!')
            win = True
        if turn == player1:
            turn = player2
        else:
            turn = player1


game()
