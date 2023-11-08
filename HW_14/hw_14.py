from random import randint, choice


class Chess:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.figures = ['♔', '♕', '♖', '♗', '♘', '♙', '♚', '♛', '♜', '♝', '♞', '♟']
        self.kings = ['♔', '♚']

    def set_w_b_kings(self):
        for king in self.kings:
            row = randint(0, 7)
            col = randint(0, 7)
            while self.board[row][col] != ' ':
                row = randint(0, 7)
                col = randint(0, 7)
            self.board[row][col] = king

    def set_figures(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        for num_figures in range(randint(10, 20)):
            row = randint(0, 7)
            col = randint(0, 7)
            while self.board[row][col] != ' ':
                row = randint(0, 7)
                col = randint(0, 7)
            self.board[row][col] = choice(self.figures)
        self.set_w_b_kings()  # Добавляем по 1 белому и черному королю

    def print_board(self):
        print('   ', end='')
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            print(i.center(6), end='')
        print()
        print('  ' + '┌' + '─────┐' * 8)
        for i in range(8):
            print(f'{8 - i} │', end='')
            for j in range(8):
                print(f'{self.board[i][j].center(5)}│', end='')
            print(f' {8 - i}')
            if i < 7:
                print('  ├' + '─────┤' * 8)
        print('  ' + '└' + '─────┘' * 8)
        print('   ', end='')
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            print(i.center(6), end='')
        print()


if __name__ == '__main__':
    board = Chess()
    print('Доска №1'.center(55))
    board.set_figures()
    board.print_board()
    print('Доска №2'.center(55))
    board.set_figures()
    board.print_board()
    print('Доска №3'.center(55))
    board.set_figures()
    board.print_board()
