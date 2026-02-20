# Daniel Hayes
# Functions to assist in controls for run function.
import chess

def get_square_moves(x,y,width,height,board,team):
    """
    This function takes the click location on event in pygame and returns the legal from that square.

    input: coordinates of click, height and width of squares, and team which determines board setup.

    returns: list of legal moves from that square
    """
    if(team):
        
        file = int((height*8-y)/height)
        rank = int(x/width)
    else:
        file = int(y/height)
        rank = int((8*width-x)/width)
        

    print("x: ",x," y: ",y)
    print("rank: ",rank," file: ",file)
    print(chess.square(rank,file))

    moves_from_square = [move for move in board.legal_moves if move.from_square == chess.square(rank,file)]

    return moves_from_square

def get_move(x,y,width,height,moves,team):
    
    if(team):
        file = int((height*8-y)/height)
        rank = int(x/width)
    else:
        file = int(y/height)
        rank = int((8*width-x)/width)
    
    for move in moves:
        if move.to_square == chess.square(rank,file):
            return move
    return None