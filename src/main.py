import pygame
import sys
from const import *
from board import Board
from game import Game


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tic tac toe')
        self.board = Board()
        self.game = Game(self.board)

    def mainloop(self):
        game = self.game
        board = self.board
        screen = self.screen
        game.show_bg(screen)
        while True:
            if game.check_set_win():
                game.print_win(game.winner, screen)
            elif game.check_tie():
                game.print_tie(screen)
            else:
                game.show_signs(screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and game.check_set_win() == False and game.check_tie() == False:
                    clicked_x = event.pos[0] // SQSIZE
                    clicked_y = event.pos[1] // SQSIZE
                    if board.squares[clicked_y][clicked_x] == -10:
                        board.squares[clicked_y][clicked_x] = 1 if game.turn == 'X' else 2
                        # blit it
                        game.show_signs(screen)
                        if game.check_set_win():
                            game.print_win(game.winner, screen)
                        if game.check_tie():
                            game.print_tie(screen)
                        game.next_turn()
                    if game.check_set_win():
                        game.print_win(game.winner, screen)
                    if game.check_tie():
                        game.print_tie(screen)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



main = Main()
main.mainloop()
