import pygame
from const import *
from board import Board
class Game:
    def __init__(self, board):
        # init game
        self.turn = 'X'
        self.winner = ''
        self.board = board

    def blit_move(self, surface, sign, row, col):
        mark = X_IMG if sign == 'X' else O_IMG
        img = pygame.image.load(mark)
        img = pygame.transform.scale(img, (SQSIZE, SQSIZE))
        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
        img_rect = img.get_rect(center = img_center)
        surface.blit(img, img_rect)
        pygame.display.update()
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (160, 160, 160)
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)
                pygame.display.update()

    def show_signs(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col] != -10:
                    sign = 'X' if self.board.squares[row][col] == 1 else 'O'
                    self.blit_move(surface, sign, row, col)
    def next_turn(self):
        self.turn = 'X' if self.turn == 'O' else 'O'
    def check_set_win(self):
        opt = ['X', 'O']
        for sign in opt:
            for i in [0,1,2]:
                if self.board.squares[i][0] + self.board.squares[i][1] + self.board.squares[i][2] == 3:
                    self.winner = 'X'
                    return True
                if self.board.squares[0][i] + self.board.squares[1][i] + self.board.squares[2][i] == 3:
                    self.winner = 'X'
                    return True

                if self.board.squares[i][0] + self.board.squares[i][1] + self.board.squares[i][2] == 6:
                    self.winner = 'O'
                    return True
                if self.board.squares[0][i] + self.board.squares[1][i] + self.board.squares[2][i] == 6:
                    self.winner = 'O'
                    return True
            if self.board.squares[0][0] + self.board.squares[1][1] + self.board.squares[2][2] == 3:
                self.winner = 'X'
                return True
            if self.board.squares[0][2] + self.board.squares[2][0] + self.board.squares[1][1] == 3:
                self.winner = 'X'
                return True

            if self.board.squares[0][0] + self.board.squares[1][1] + self.board.squares[2][2] == 6:
                self.winner = 'O'
                return True
            if self.board.squares[0][2] + self.board.squares[2][0] + self.board.squares[1][1] == 6:
                self.winner = 'O'
                return True
        return False

    def print_win(self, winner, surface):
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render('Winner is ' + self.winner, True,'Green')
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)
        surface.blit(text, text_rect)
        pygame.display.update()