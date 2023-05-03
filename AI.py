import math
from Board import Board
from ChessPiece import *
from functools import wraps
from Logger import Logger, BoardRepr
import random


logger = Logger()

# stores the previous game states
def log_tree(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        board: Board = args[0]
        if board.log:
            depth = args[1]
            write_to_file(board, depth)
        return func(*args, **kwargs)
    return wrapper

# write moves to the file
def write_to_file(board: Board, current_depth):
    global logger
    if board.depth == current_depth:
        logger.clear()
    board_repr = BoardRepr(board.unicode_array_repr(), current_depth, board.evaluate())
    logger.append(board_repr)


@log_tree
def minimax(board, depth, alpha, beta, max_player, save_move, data):
# minimax algorithm with alpha beta pruning
    if depth == 0 or board.is_terminal():
        data[1] = board.evaluate()
        return data
    # maximizing 
    if max_player:
        max_eval = -math.inf
        for i in range(8): # iterating through pieces of black color
            for j in range(8): # Also evaluating response of every white color piece available for each black color piece
                if isinstance(board[i][j], ChessPiece) and board[i][j].color != board.get_player_color():
                    piece = board[i][j]
                    moves = piece.filter_moves(piece.get_moves(board), board)
                    for move in moves:
                        board.make_move(piece, move[0], move[1], keep_history=True)
                        evaluation = minimax(board, depth - 1, alpha, beta, False, False, data)[1]
                        if save_move:
                            if evaluation >= max_eval:
                                if evaluation > data[1]:
                                    data.clear()
                                    data[1] = evaluation
                                    data[0] = [piece, move, evaluation]
                                elif evaluation == data[1]:
                                    data[0].append([piece, move, evaluation])
                        board.unmake_move(piece)
                        max_eval = max(max_eval, evaluation)
                        alpha = max(alpha, evaluation)
                        if beta <= alpha: # pruning the unnecessary branches
                            break
        return data
    else:
        # minimizing 
        min_eval = math.inf
        for i in range(8):
            for j in range(8):
                if isinstance(board[i][j], ChessPiece) and board[i][j].color == board.get_player_color():
                    piece = board[i][j]
                    moves = piece.get_moves(board)
                    for move in moves:
                        board.make_move(piece, move[0], move[1], keep_history=True)
                        evaluation = minimax(board, depth - 1, alpha, beta, True, False, data)[1]
                        board.unmake_move(piece)
                        min_eval = min(min_eval, evaluation)
                        beta = min(beta, evaluation)
                        if beta <= alpha:
                            break
        return data

# basic function to get the best move. It depends on the board state, history and depth value
def get_ai_move(board):
    moves = minimax(board, board.depth, -math.inf, math.inf, True, True, [[], 0])
    if board.log:
        logger.write()
    # moves = [[pawn, move, move_score], [..], [..],[..], total_score]
    if len(moves[0]) == 0:
        return False
    best_score = max(moves[0], key=lambda x: x[2])[2]
    piece_and_move = random.choice([move for move in moves[0] if move[2] == best_score])
    piece = piece_and_move[0]
    move = piece_and_move[1]
    if isinstance(piece, ChessPiece) and len(move) > 0 and isinstance(move, tuple):
        board.make_move(piece, move[0], move[1])
    return True


