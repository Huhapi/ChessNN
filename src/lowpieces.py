# Daniel Hayes
# 10/10/25

# Play best moves at 5 or less pieces.

import chess # type: ignore
import chess.syzygy # type: ignore


def endgame_move(fen):
    """
    This function requires the input to be a fen chess board representation with 5 or less pieces.

    input: Chess board Fen with 5 or less pieces.

    returns: best move object. 
    """
    board = chess.Board(fen)
    tablebase = chess.syzygy.open_tablebase("src/syzygy/")
    moves = []
    values = []

    for move in board.legal_moves:
        board.push(move)
        try:
            dtz = tablebase.probe_dtz(board)
            moves.append(move)
            values.append(dtz)
        except:
            pass
        board.pop()
    
    return moves[values.index(max(values))] if values else None
