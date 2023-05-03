

import graphics
import sys


from square import Square 

import pygame
from Board import *

class Main:

    def __init__(self):
        pass

    def play_AI(self):
        keep_playing = True
        board = Board(game_mode=0, ai=True, depth=2, log=True)  
        # game_mode = 0 means human plays white while game_mode = 1 means computer plays white
        # depth is the deepness of the minimax tree

        while keep_playing:
           
            graphics.initialize()
            board.place_pieces()
            graphics.draw_background(board)
            keep_playing = graphics.start(board)
        sys.exit()
            
if __name__ == '__main__':
    main = Main()
    
    
    main.play_AI()
    
        
