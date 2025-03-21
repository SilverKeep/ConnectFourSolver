import os

#0-INDEXED
#Indexing will be bottom to top, decreasing index number as it goes up
#0 represents no player, 'x' represents x, 'o' represents 'o'

class ConnectFour:
    board = [' ']
    rows = 6
    cols = 7
    playing = True

    def __init__(self):
        self.board = [[' ' for _ in range(self.rows)] for _ in range(self.cols)]
    
    def play_move(self, position, player):
        for i in range(self.rows - 1, -1, -1):
            if self.board[i][position] == ' ':
                self.board[i][position] = player
                return True
        return False
    
    def check_win(self):
        #horizontal
        for i in self.board:
            row = "".join(i)
            if "xxxx" in row:
                return 'x'
            if "oooo" in row:
                return 'o'
        
        #vertical
        for i in range(self.cols):
            col = "".join([self.board[j][i] for j in range(len(self.board))])
            if "xxxx" in col:
                return 'x'
            if "oooo" in col:
                return 'o'
        
        #diagonal
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                diag = [self.board[r + i][c + i] for i in range(4)]
                if "xxxx" == "".join(diag):
                    return 'x'
                if "oooo" == "".join(diag):
                    return 'o'

        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                diag = [self.board[r - i][c + i] for i in range(4)]
                if "xxxx" == "".join(diag):
                    return 'x'
                if "oooo" == "".join(diag):
                    return 'o'
                
        return ' '
    
    def print_board(self):
        os.system('clear')
        for i in self.board:
            print("|", end="")
            for j in i:
                print(j, end="|")
            print()
        print(" 1 2 3 4 5 6 7")
    
    def play_game(self):
        turn = 'x'
        filled = 0
        while self.playing and filled < self.rows * self.columns:
            self.print_board()
            while True:
                print(turn + "'s turn to move (1-7):", end=" ")
                move = int(input()) - 1
                if self.play_move(move, turn):
                    break
            
            result = self.check_win()
            if result == 'x':
                self.print_board()
                print("x wins")
                self.playing = False
            if result == 'o':
                self.print_board()
                print("o wins")
                self.playing = False
            
            filled += 1
            if turn == 'x': turn = 'o'
            else: turn = 'x'

game = ConnectFour()
game.play_game()