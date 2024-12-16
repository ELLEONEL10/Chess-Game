import os
import pygame
from pygame.locals import *
from chess import Chess

class Utils:
    """Utility class to handle mouse and keyboard events"""

    def __init__(self):
        pass

    def left_click_event(self):
        """Check if left mouse button is clicked"""
        return pygame.mouse.get_pressed()[0] == 1

    def get_mouse_event(self):
        """Return current mouse position"""
        return pygame.mouse.get_pos()


class Game:
    def __init__(self):
        # screen dimensions
        screen_width = 640
        screen_height = 750
        # flag to know if game menu has been shown
        self.menu_showed = False
        # flag to set game loop
        self.running = True
        # base folder for program resources
        self.resources = "res"

        # initialize game window
        pygame.display.init()
        # initialize font for text
        pygame.font.init()

        # create game window
        self.screen = pygame.display.set_mode([screen_width, screen_height])

        # title of window
        window_title = "Chess"
        # set window caption
        pygame.display.set_caption(window_title)

        # get location of game icon
        icon_src = os.path.join(self.resources, "chess_icon.png")
        # load game icon
        icon = pygame.image.load(icon_src)
        # set game icon
        pygame.display.set_icon(icon)
        # update display
        pygame.display.flip()
        # set game clock
        self.clock = pygame.time.Clock()

    def start_game(self):
        """Function containing main game loop""" 
        # chess board offset
        self.board_offset_x = 0
        self.board_offset_y = 50
        self.board_dimensions = (self.board_offset_x, self.board_offset_y)
        
        # get location of chess board image
        board_src = os.path.join(self.resources, "board.png")
        # load the chess board image
        self.board_img = pygame.image.load(board_src).convert()

        # get the width of a chess board square
        square_length = self.board_img.get_rect().width // 8

        # initialize list that stores all places to put chess pieces on the board
        self.board_locations = []

        # calculate coordinates of each square on the board
        for x in range(0, 8):
            self.board_locations.append([])
            for y in range(0, 8):
                self.board_locations[x].append([self.board_offset_x + (x * square_length), 
                                                self.board_offset_y + (y * square_length)])

        # get location of image containing the chess pieces
        pieces_src = os.path.join(self.resources, "pieces.png")
        # create class object that handles the gameplay logic
        self.chess = Chess(self.screen, pieces_src, self.board_locations, square_length)

        # game loop
        while self.running:
            self.clock.tick(5)
            # poll events
            for event in pygame.event.get():
                # get keys pressed
                key_pressed = pygame.key.get_pressed()
                # check if the game has been closed by the user
                if event.type == pygame.QUIT or key_pressed[K_ESCAPE]:
                    # set flag to break out of the game loop
                    self.running = False
                elif key_pressed[K_SPACE]:
                    self.chess.reset()
            
            winner = self.chess.winner

            if self.menu_showed == False:
                self.menu()
            elif len(winner) > 0:
                self.declare_winner(winner)
            else:
                self.game()

            # update display
            pygame.display.flip()
            # update events
            pygame.event.pump()

        # call method to stop pygame
        pygame.quit()

    def menu(self):
        """Method to show game menu"""
        # Load background image
        bg_image = pygame.image.load(os.path.join(self.resources, "bg.png")).convert()  # Replace with your background image
        bg_rect = bg_image.get_rect()
        
        # Set the background image
        self.screen.blit(bg_image, bg_rect)

        # black color for buttons
        black_color = (0, 0, 0)

        # height and width for buttons
        button_width = 300
        button_height = 50
        button_margin = 20  # margin between buttons

        # Create button positions and align them to the center
        start_btn1 = pygame.Rect((self.screen.get_width() - button_width) // 2, 300, button_width, button_height)  # Multiplayer
        start_btn2 = pygame.Rect((self.screen.get_width() - button_width) // 2, 300 + button_height + button_margin, button_width, button_height)  # AI Game
        start_btn3 = pygame.Rect((self.screen.get_width() - button_width) // 2, 300 + 2 * (button_height + button_margin), button_width, button_height)  # Load Game
        about_btn = pygame.Rect((self.screen.get_width() - button_width) // 2, 300 + 3 * (button_height + button_margin), button_width, button_height)  # About/Info

        # show play buttons
        pygame.draw.rect(self.screen, black_color, start_btn1)
        pygame.draw.rect(self.screen, black_color, start_btn2)
        pygame.draw.rect(self.screen, black_color, start_btn3)
        pygame.draw.rect(self.screen, black_color, about_btn)

        # white color for text
        white_color = (255, 255, 255)
        # create fonts for texts
        font_path = os.path.join(self.resources, "font.otf")
        big_font = pygame.font.Font(font_path, 35)
        small_font = pygame.font.Font(font_path, 20)
        
        # create text to be shown on the game menu
        welcome_text = big_font.render("Chess Game", False, white_color)
        start_btn1_label = small_font.render("Multiplayer", True, white_color)
        start_btn2_label = small_font.render("AI Game", True, white_color)
        start_btn3_label = small_font.render("Load Game", True, white_color)
        about_btn_label = small_font.render("About", True, white_color)
        
        # show welcome text
        self.screen.blit(welcome_text, 
                         ((self.screen.get_width() - welcome_text.get_width()) // 2, 
                          150))

        # show text on the buttons
        self.screen.blit(start_btn1_label, 
                         ((start_btn1.x + (start_btn1.width - start_btn1_label.get_width()) // 2, 
                           start_btn1.y + (start_btn1.height - start_btn1_label.get_height()) // 2)))

        self.screen.blit(start_btn2_label, 
                         ((start_btn2.x + (start_btn2.width - start_btn2_label.get_width()) // 2, 
                           start_btn2.y + (start_btn2.height - start_btn2_label.get_height()) // 2)))

        self.screen.blit(start_btn3_label, 
                         ((start_btn3.x + (start_btn3.width - start_btn3_label.get_width()) // 2, 
                           start_btn3.y + (start_btn3.height - start_btn3_label.get_height()) // 2)))

        self.screen.blit(about_btn_label, 
                         ((about_btn.x + (about_btn.width - about_btn_label.get_width()) // 2, 
                           about_btn.y + (about_btn.height - about_btn_label.get_height()) // 2)))

        # Get mouse and keyboard events
        key_pressed = pygame.key.get_pressed()
        util = Utils()

        # Check if left mouse button was clicked
        if util.left_click_event():
            # Call function to get mouse event
            mouse_coords = util.get_mouse_event()

            # Check if any button was clicked
            if start_btn1.collidepoint(mouse_coords[0], mouse_coords[1]):
                pygame.draw.rect(self.screen, white_color, start_btn1, 3)
                self.menu_showed = True
            elif key_pressed[K_RETURN]:
                self.menu_showed = True
            elif about_btn.collidepoint(mouse_coords[0], mouse_coords[1]):
                self.show_about()

    def game(self):
        """Method to run the game"""
        # background color
        color = (0, 0, 0)
        # set background color
        self.screen.fill(color)
        
        # show the chess board
        self.screen.blit(self.board_img, self.board_dimensions)

        # call the chess play turn method
        self.chess.play_turn()
        # draw pieces on the chess board
        self.chess.draw_pieces()  # Ensure this is implemented in Chess class

    def declare_winner(self, winner):
        """Method to declare the winner"""
        # background color
        bg_color = (255, 255, 255)
        # set background color
        self.screen.fill(bg_color)
        # black color
        black_color = (0, 0, 0)
        # coordinates for play again button
        reset_btn = pygame.Rect(250, 300, 140, 50)
        # show reset button
        pygame.draw.rect(self.screen, black_color, reset_btn)

        # white color
        white_color = (255, 255, 255)
        # create fonts for texts
        font_path = os.path.join(self.resources, "font.otf")
        big_font = pygame.font.Font(font_path, 35)
        small_font = pygame.font.Font(font_path, 20)
        

        # text to show winner
        text = winner + " wins!" 
        winner_text = big_font.render(text, False, black_color)

        # create text to be shown on the reset button
        reset_label = "Play Again"
        reset_btn_label = small_font.render(reset_label, True, white_color)

        # show winner text
        self.screen.blit(winner_text, 
                         ((self.screen.get_width() - winner_text.get_width()) // 2, 
                          150))
        
        # show text on the reset button
        self.screen.blit(reset_btn_label, 
                         ((reset_btn.x + (reset_btn.width - reset_btn_label.get_width()) // 2, 
                           reset_btn.y + (reset_btn.height - reset_btn_label.get_height()) // 2)))


        # Get mouse and keyboard events
        key_pressed = pygame.key.get_pressed()
        util = Utils()

        # Check if left mouse button was clicked
        if util.left_click_event():
            # Call function to get mouse event
            mouse_coords = util.get_mouse_event()

            # Check if reset button was clicked
            if reset_btn.collidepoint(mouse_coords[0], mouse_coords[1]):
                pygame.draw.rect(self.screen, white_color, reset_btn, 3)
                self.menu_showed = False
            elif key_pressed[K_RETURN]:
                self.menu_showed = False

            # Reset game
            self.chess.reset()
            self.chess.winner = ""


    def show_about(self):
        """Method to show info about the program and the repo as a popup window"""
        # pop-up window dimensions
        popup_width = 400
        popup_height = 200
        popup_x = (self.screen.get_width() - popup_width) // 2
        popup_y = (self.screen.get_height() - popup_height) // 2

        # create the pop-up surface
        popup = pygame.Surface((popup_width, popup_height))
        popup.fill((255, 255, 255))  # white background
        pygame.draw.rect(popup, (0, 0, 0), popup.get_rect(), 5)  # border

        # add close and minimize buttons
        close_btn = pygame.Rect(popup_width - 30, 10, 20, 20)
        pygame.draw.rect(popup, (255, 0, 0), close_btn)  # red close button
        minimize_btn = pygame.Rect(popup_width - 60, 10, 20, 20)
        pygame.draw.rect(popup, (255, 255, 0), minimize_btn)  # yellow minimize button

        # create the text to show in the popup
        about_text = "Programmed by Fadi Abbara And Anas Zahran." 
        "\nGithub Repo: https://github.com/ELLEONEL10/Chess-Game.git"
        font_path = os.path.join(self.resources, "font.otf")

        # draw the popup onto the screen
        self.screen.blit(popup, (popup_x, popup_y))
        pygame.display.flip()

        # waiting for input event to close the window
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    waiting_for_input = False
                elif event.type == pygame.KEYDOWN:
                    waiting_for_input = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_coords = pygame.mouse.get_pos()
                    # close button clicked
                    if close_btn.collidepoint(mouse_coords):
                        waiting_for_input = False
                    # minimize button clicked
                    if minimize_btn.collidepoint(mouse_coords):
                        pygame.display.iconify()  # Minimize window
