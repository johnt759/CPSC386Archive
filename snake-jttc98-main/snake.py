#!/usr/bin/env python3
#
# John Tu
# CPSC 386-01
# 2021-05-11
# jttc98@csu.fullerton.edu
# @jttc98
#
# 05-Snake Game
#
# Snake Game written in pygame style
"""Here is my snake game created via PyGame."""
import sys
import random
import os
import json # Needed to do json operations
from datetime import date # Needed to get current date
from datetime import datetime # Needed to get current time
import pygame

pygame.init()

# Define the screen height and width constants below.
SCREEN_X = 800
SCREEN_Y = 600

WIN_DISPLAY = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("Snake Game in Pygame")

# Declare the following color variables.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT_TEXT = pygame.font.SysFont("georgia", 20)

# This variable is needed to keep the game moving.
FPS_CLOCK = pygame.time.Clock()

DEFAULT_FPS = 25

OBJ_SIZE = 10

class Snake:
    """This class contains functions and definitions for the Snake.

    The snake is placed at its default locations when the game starts.
    If player presses the arrow keys, move the snake by changing its coordinates.
    """

    def __init__(self, x_pos=400, y_pos=200):
        """The initializer will set up the snake."""
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_dir = 0
        self.y_dir = 0
        self.snake_body = [[self.x_pos, self.y_pos], [self.x_pos-200, self.y_pos],\
        [self.x_pos-400, self.y_pos]]
        self.snake_head = [self.x_pos, self.y_pos]
        self.snake_dir = "east" # Move the snake right by default.
        self.snake_len = 1

    def draw_body(self):
        """Draw the snake's new body in the game.

        Always update the snake's current position to ensure
        that it moves properly along the area.
        """
        WIN_DISPLAY.fill(BLUE)

        self.x_pos += self.x_dir
        self.y_pos += self.y_dir

        # Update the snake's head whenever it moves.
        self.snake_head = [self.x_pos, self.y_pos]
        self.snake_body.append(self.snake_head)

        if len(self.snake_body) > self.snake_len:
            del self.snake_body[0]

        # Now draw out the snake's body and display on screen.
        for body in self.snake_body:
            pygame.draw.rect(WIN_DISPLAY, GREEN, [body[0], body[1], OBJ_SIZE, OBJ_SIZE])

    def move_snake(self, direction):
        """Move the snake in any direction if arrow key is pressed.

        Also, ensure the snake does not move over its own body
        by checking if the snake is going in the opposite direction.
        """
        if direction == "east" and self.snake_dir != "west":
            self.snake_dir = "east"
        elif direction == "west" and self.snake_dir != "east":
            self.snake_dir = "west"
        elif direction == "north" and self.snake_dir != "south":
            self.snake_dir = "north"
        elif direction == "south" and self.snake_dir != "north":
            self.snake_dir = "south"

        if self.snake_dir == "west":
            self.x_dir -= OBJ_SIZE
            self.y_dir = 0
        elif self.snake_dir == "east":
            self.x_dir += OBJ_SIZE
            self.y_dir = 0
        elif self.snake_dir == "north":
            self.x_dir = 0
            self.y_dir -= OBJ_SIZE
        elif self.snake_dir == "south":
            self.x_dir = 0
            self.y_dir += OBJ_SIZE

    def collide_wall(self):
        """Check if the snake collides into the wall.

        To be more specific, if the snake collides into the
        boundaries of the game, then return true. Otherwise,
        return false.
        """
        if self.snake_head[0] < 0:
            return True
        elif self.snake_head[0] >= SCREEN_X:
            return True
        elif self.snake_head[1] < 0:
            return True
        elif self.snake_head[1] >= SCREEN_Y:
            return True
        else:
            return False

    def collide_self(self):
        """Check if the snake collides into its own tail.

        If the snake's head touches any of its body, return true.
        Otherwise, return false. If only the head exists, return
        false because the length of the snake's body is 1 if only
        the head exists.
        """
        if len(self.snake_body) == 1:
            return False

        # Start after the snake's head in the body when checking
        # for head colliding with the body.
        for body in self.snake_body[1:]:
            if self.snake_head[0] == body[0] and self.snake_head[0] == body[1]:
                return True
        return False

    def collide_apple(self, obj):
        """Check if the snake eats the apple.

        If the snake's head collides with the apple, then increment
        the score by 1 and generate the new apple across the area.
        """
        if [self.snake_head[0], self.snake_head[1]] == [obj[0], obj[1]]:
            return True
        return False

    def add_body(self):
        """Append the new body segment into the snake body."""
        self.snake_body.append([self.x_pos, self.y_pos])

class Food:
    """This class contains functions and definitions for the Food."""
    def __init__(self):
        """The initializer will set up the food."""
        self.x_pos = random.randrange(0, SCREEN_X, OBJ_SIZE)
        self.y_pos = random.randrange(0, SCREEN_Y, OBJ_SIZE)
        self.apple_pos = [0, 0]
        self.is_eaten = False

    def draw_apple(self):
        """Draw the food's coordinates and place it anywhere in the game."""
        pygame.draw.rect(WIN_DISPLAY, RED, [self.x_pos, self.y_pos, OBJ_SIZE, OBJ_SIZE])

    def new_apple(self, is_eaten):
        """Draw the new apple when the snake eats the apple.

        Always randomize the new coordinates when placing the apple
        anywhere in the game area.
        """
        if is_eaten:
            self.apple_pos = self.get_loc()
            pygame.draw.rect(WIN_DISPLAY, BLUE, [self.apple_pos[0], self.apple_pos[1],\
                OBJ_SIZE, OBJ_SIZE])
            is_eaten = False
        self.x_pos = random.randrange(0, SCREEN_X, OBJ_SIZE)
        self.y_pos = random.randrange(0, SCREEN_Y, OBJ_SIZE)

    def get_loc(self):
        """Return the food's current position."""
        return [self.x_pos, self.y_pos]

def show_instructions():
    """This function will display the instructions for Snake.

    Always call this function when the game starts for the first time
    or the player dies and the game restarts by itself.
    """
    title = pygame.font.SysFont("georgia", 50)
    instruct = pygame.font.SysFont("georgia", 20)
    title_text = title.render("Welcome to Snake!", 1, WHITE)
    instruct_text_1 = instruct.render("Score as many points possible", 1, WHITE)
    instruct_text_2 = instruct.render("without touching the walls.", 1, WHITE)
    instruct_text_3 = instruct.render("Eat the apple in order to score points.", 1, WHITE)
    instruct_text_4 = instruct.render("As you eat, your body will grow", 1, WHITE)
    instruct_text_5 = instruct.render("longer, so watch out!", 1, WHITE)
    instruct_text_6 = instruct.render("If you collide at your tail or at the wall,", 1, WHITE)
    instruct_text_7 = instruct.render("then the game's over!", 1, WHITE)

    WIN_DISPLAY.fill(BLACK)
    WIN_DISPLAY.blit(title_text, (200, 40))
    WIN_DISPLAY.blit(instruct_text_1, (200, 160))
    WIN_DISPLAY.blit(instruct_text_2, (200, 180))
    WIN_DISPLAY.blit(instruct_text_3, (200, 200))
    WIN_DISPLAY.blit(instruct_text_4, (200, 220))
    WIN_DISPLAY.blit(instruct_text_5, (200, 240))
    WIN_DISPLAY.blit(instruct_text_6, (200, 260))
    WIN_DISPLAY.blit(instruct_text_7, (200, 280))

    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(5000)
    WIN_DISPLAY.fill(BLUE)
    pygame.display.update()

def game_over(point):
    """This function is called only when the game is over.

    It occurs anytime if the snake collides into the wall or
    it collides into its own tail. If so, then after some time
    has passed, save the scores in the json file and restart the game.
    """
    end_font = pygame.font.SysFont("georgia", 30)
    game_over_text = end_font.render("You Died!", 1, WHITE)
    score_text = end_font.render("You scored {} points".format(point), 1, WHITE)
    restart_text = end_font.render("Restarting...", 1, WHITE)
    WIN_DISPLAY.fill(BLACK)
    WIN_DISPLAY.blit(game_over_text, (290, 80))
    WIN_DISPLAY.blit(score_text, (290, 160))
    WIN_DISPLAY.blit(restart_text, (290, 240))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(5000)

def create_scores():
    """This function is called to create a json scores file.

    If the json file doesn't exist, then create a new json file.
    """
    if not os.path.exists("highscores.json"):
        stats = {"Highscores": []}
        with open("highscores.json", "w") as file:
            json.dump(stats, file)

def update_scores(point):
    """This function is called to update the json scores file.

    Save each entry of the highscores with the date and time played, and
    the number of points earned during the gameplay.
    """
    current_date = date.today()
    current_time = datetime.now().time()
    today_time = current_time.strftime("%H:%M:%S")
    new_scores = {"Date": current_date, "Time": today_time, "Points": point}
    with open("highscores.json", "r+") as file:
        stats = json.load(file)
        temp = stats["Highscores"]
        temp.append(new_scores)

    # When writing into the json, tidy the format by indenting.
    # Also, default to string in order to serialize the date played.
    with open("highscores.json", "w") as file:
        json.dump(stats, file, indent=2, default=str)

def main():
    """The main function is where the game of Snake runs.

    Keep the game running by setting the while loop variable
    to true until the user decides to close the program. If so,
    then break out of loop, and then quit the program entirely.
    """
    keep_playing = True
    while keep_playing:
        still_playing = True

        player = Snake()
        apple = Food()

        show_instructions()
        game_score = player.snake_len - 1

        create_scores()

        while still_playing:
            # Check if there is any events detected such as key pressed or the user
            # clicks on the minimize, maximize, or close buttons.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # If the player clicks on the close button,
                    # set the boolean variable to false, break
                    # out of the loop, and quit the game.
                    still_playing = False
                    keep_playing = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.move_snake("west")
                    if event.key == pygame.K_RIGHT:
                        player.move_snake("east")
                    if event.key == pygame.K_UP:
                        player.move_snake("north")
                    if event.key == pygame.K_DOWN:
                        player.move_snake("south")
                    if event.key == pygame.K_ESCAPE:
                        still_playing = False
                        keep_playing = False
                        break

            if player.collide_wall():
                # Display the player's score during the game over screen.
                # After that, save the score into the json file.
                still_playing = False
                game_over(game_score)
                update_scores(game_score)
                break

            if player.collide_apple(apple.get_loc()):
                apple.new_apple(True)
                game_score += 1
                apple.draw_apple()
                player.add_body()

            player.draw_body()
            apple.draw_apple()

            score_text = FONT_TEXT.render("Points: {}".format(game_score), 1, WHITE)
            WIN_DISPLAY.blit(score_text, (350, 500))

            pygame.display.update()
            FPS_CLOCK.tick(DEFAULT_FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
