# Daniel Hayes 
# This file holds the object which creates the window for the chess program.
import chess # type: ignore
import pygame # type: ignore
import os 



        
def drawPieces(screen, square_size, images, board, team):
    """ This function draws the pieces on board.
    input: the board and the piece image dictionary.
    returns: nothing - draws the pictures related with the squares on the board.
    """
    
    if(team):
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                location = [chess.square_file(square)*square_size[0],7*square_size[1]-chess.square_rank(square)*square_size[1]]
                pic = images[piece.symbol()]
                screen.blit(pic,location)   
    else:
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                location = [int(7*square_size[0]-chess.square_file(square)*square_size[0]),chess.square_rank(square)*square_size[1]]
                pic = images[piece.symbol()]
                screen.blit(pic,location)          

def highLightMoves(screen, moves, team, squareSize):
    """ Takes in the screen, the list of moves and highlight the potential to squares.
    input: screen, list of moves, height and width of squares.
    output: highlighted squares
    """
    highlight = pygame.Surface(squareSize) 
    highlight.fill(pygame.Color("green"))
    if len(moves) > 0:
        if(team):
            for move in moves:
                square = move.to_square
                screen.blit(highlight, (chess.square_file(square)*squareSize[0], 7*squareSize[1]-chess.square_rank(square)*squareSize[1]))
        else:
            for move in moves:
                square = move.to_square
                screen.blit(highlight, (int(7*squareSize[0]-chess.square_file(square)*squareSize[0]),chess.square_rank(square)*squareSize[1]))

def loadImages(square_size):
    """
    Loads the images for the pieces, with keys based off from the pieces names on the board positions.
    Args: None
    returns: a dictionary of loaded piece images in pygames.
    """
        
    cwd = os.getcwd() 
    print("Current working directory:", cwd) 
    images = {
            "Q":pygame.transform.scale(pygame.image.load(cwd + "\\src\\pics\\" + "Q" + ".png"), square_size),
                "R":pygame.transform.scale(pygame.image.load(cwd + "\\src\\pics\\" + "R" + ".png"), square_size),
                "N":pygame.transform.scale(pygame.image.load(cwd + "\\src\\pics\\" + "N" + ".png"), square_size),
                "K":pygame.transform.scale(pygame.image.load(cwd + "\\src\\pics\\" + "K" + ".png"), square_size),
                "B":pygame.transform.scale(pygame.image.load(cwd + "\\src\\pics\\" + "B" + ".png"), square_size),
                "P":pygame.transform.scale(pygame.image.load(cwd + "\\src\\pics\\" + "P" + ".png"), square_size),
                "r":pygame.transform.scale(pygame.image.load(cwd + "\\src\\pics\\" + "BR" + ".png"), square_size),
                "n":pygame.transform.scale(pygame.image.load(cwd + "\\src\\pics\\" + "BN" + ".png"), square_size),
                "p":pygame.transform.scale(pygame.image.load(cwd + "\\src\\pics\\" + "BP" + ".png"), square_size),
                "k":pygame.transform.scale(pygame.image.load(cwd + "\\src\\pics\\" + "BK" + ".png"), square_size),
                "q":pygame.transform.scale(pygame.image.load(cwd + "\\src\\pics\\" + "BQ" + ".png"), square_size),
                "b":pygame.transform.scale(pygame.image.load(cwd + "\\src\\pics\\" + "BB" + ".png"), square_size)
            }

    return(images)


def setupBoard(screen,squareSize):
    """ 
    Prints the checkered chess board on the screen.
    args: current pygame screen(self) and the length of the side of the squares.
    returns: nothing 
    """
        
    white = pygame.Color(255, 255, 255)
    screen.fill(pygame.Color("darkblue"))
    for square in range(64):
        if square%2 == 0:
            if 7 < square < 15 or 23 < square < 31 or 39 < square < 47 or 55 < square < 63:
                x = int(((1+square%8)*squareSize[0]))
                y = (int(square/8))*squareSize[1]
                pygame.draw.rect(screen,white,pygame.Rect(x,y,squareSize[0],squareSize[1]))
            else: 
                x = int((square%8*squareSize[0]))
                y = (int(square/8))*squareSize[1]
                pygame.draw.rect(screen,white,pygame.Rect(x,y,squareSize[0],squareSize[1]))

        pygame.display.update()
        
    
        
