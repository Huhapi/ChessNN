# Daniel Hayes pygames chess implementation
import chess # type: ignore
import theview 
import pygame # type: ignore
import sys
import controls 
import getNNmove as nn

def run():
    """
    This function uses window class to create the window for a chess game. Where the user can interact via
    clicking on pieces to move them. It also uses the engine class to find moves to play against the user.
    This is the controller, window is the view, and engine is the model.

    args: none

    returns: none

    """

    # Initialize board
    board = chess.Board()

    # Initialize depth value:
    depth = 4

    play_computer = True
    # Determines if user playing black or white. True for white
    team = False

    # Initialize the engine
    chess_engine = nn.retrieveMove()

    # Set the window size
    WIDTH = 500
    HEIGHT = 500
    window_size = (WIDTH, HEIGHT) # adjustable
    
    pygame.init()
    
    screen = pygame.display.set_mode(window_size,pygame.RESIZABLE)
    
    fps_controller = pygame.time.Clock()
    
    squareSize = (int(WIDTH/8),int(HEIGHT/8)) # adjustable
    
    # Load images
    images = theview.loadImages(squareSize)

    # Setup Board squares
    theview.setupBoard(screen,squareSize)

    make_move = False

    is_instance = False

    # Initialize pieces
    theview.drawPieces(screen,squareSize,images,board,team)
    pygame.display.flip()
    # Game loop
    run = True
    while(run):
        
        for event in pygame.event.get():
            # Quit the game if the player closes the window
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit() 
            if event.type == pygame.VIDEORESIZE:
                # Adjust screen size dynamically
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                squareSize = (int(WIDTH/8),int(HEIGHT/8))
                # Setup board to match new screen dimensions
                theview.setupBoard(screen,squareSize)
                images = theview.loadImages(squareSize)
                theview.drawPieces(screen,squareSize,images,board,team)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Line up clicks with squares, move pieces, highlight potential moves.
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if board.is_game_over():
                    print(board.outcome())
                    run = False
                else:
                    if(make_move and (team == board.turn or not play_computer)):
                        move = controls.get_move(x,y,squareSize[0],squareSize[1],potential_moves,team)
                        if(move):
                            board.push(move)
                            make_move = False

                    theview.setupBoard(screen,squareSize)
                    theview.drawPieces(screen,squareSize,images,board,team)
                    potential_moves = controls.get_square_moves(x,y,squareSize[0],squareSize[1],board,team)
                    print(potential_moves)
                    if(potential_moves):
                        theview.highLightMoves(screen,potential_moves,team,squareSize)
                        theview.drawPieces(screen,squareSize,images,board,team)
                        make_move = True

            # CPU takes its turn - when play_computer is true, it is not the players team turn, and an instance of the CPU is not active.
            if team != board.turn and play_computer:
                if board.is_game_over():
                    run = False
                    print(board.outcome())
                else:
                    #is_instance = True
                    engine_move = chess_engine.getmove(board.fen()) 
                    if(engine_move):
                        chess_move = chess.Move.from_uci(engine_move)
                        board.push(chess_move)
                        theview.setupBoard(screen,squareSize)
                        theview.highLightMoves(screen,[chess_move],team,squareSize)
                        theview.drawPieces(screen,squareSize,images,board,team)


        # There is an instance of engine running, try and retrieve move for cpu.
        """if is_instance:
            await asyncio.sleep(0)                  
            cpumove = chess_engine.retrieve_move()
            if(cpumove):
                board.push(cpumove)
                is_instance = False
                theview.setupBoard(screen,squareSize)
                theview.highLightMoves(screen,[cpumove],team,squareSize)
                theview.drawPieces(screen,squareSize,images,board,team)"""

        pygame.display.update()   

        fps_controller.tick(24)




run()