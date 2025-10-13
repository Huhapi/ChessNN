# Daniel Hayes
# 10/5/25
# Board chess fen object to tensor object function.
import numpy as np
import chess
import torch

def fen_to_tensor(fen):
    """
    fen_to_tensor function converts chess library fen to tensor object.

    args: chess board fen representation
    returns: Tensor board representation
    """
    board = chess.Board(fen)
    tensor = np.zeros((18, 8, 8), dtype=np.float32)

    piece_map = {
        'P': 0, 'N': 1, 'B': 2, 'R': 3, 'Q': 4, 'K': 5,
        'p': 6, 'n': 7, 'b': 8, 'r': 9, 'q': 10, 'k': 11
    }

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            row = 7 - chess.square_rank(square)
            col = chess.square_file(square)
            tensor[piece_map[piece.symbol()]][row][col] = 1

    # Side to move
    if board.turn == chess.WHITE:
        tensor[12] = np.ones((8, 8))
    
    # Castling rights
    if board.has_kingside_castling_rights(chess.WHITE):
        tensor[13] = np.ones((8, 8))
    if board.has_queenside_castling_rights(chess.WHITE):
        tensor[14] = np.ones((8, 8))
    if board.has_kingside_castling_rights(chess.BLACK):
        tensor[15] = np.ones((8, 8))
    if board.has_queenside_castling_rights(chess.BLACK):
        tensor[16] = np.ones((8, 8))

    # En passant
    if board.ep_square:
        row = 7 - chess.square_rank(board.ep_square)
        col = chess.square_file(board.ep_square)
        tensor[17][row][col] = 1


    torch_tensor = torch.tensor(tensor).float()

    return torch_tensor



