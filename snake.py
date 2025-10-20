#!/usr/bin/env python3
"""
Snake Game - Terminal Version
Use arrow keys to control the snake
Press 'q' to quit
"""

import curses
import random
from collections import deque

class SnakeGame:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.height -= 2  # Leave space for score

        # Initialize game state
        self.reset_game()

        # Setup curses
        curses.curs_set(0)  # Hide cursor
        stdscr.nodelay(1)   # Non-blocking input
        stdscr.timeout(100) # Refresh rate

    def reset_game(self):
        # Snake starts in the middle
        start_y = self.height // 2
        start_x = self.width // 2
        self.snake = deque([(start_y, start_x)])
        self.direction = curses.KEY_RIGHT
        self.score = 0
        self.game_over = False
        self.spawn_food()

    def spawn_food(self):
        """Spawn food at a random location not occupied by snake"""
        while True:
            self.food = (
                random.randint(1, self.height - 2),
                random.randint(1, self.width - 2)
            )
            if self.food not in self.snake:
                break

    def handle_input(self):
        """Handle keyboard input"""
        key = self.stdscr.getch()

        if key == ord('q'):
            return False

        # Prevent reversing direction
        if key == curses.KEY_UP and self.direction != curses.KEY_DOWN:
            self.direction = key
        elif key == curses.KEY_DOWN and self.direction != curses.KEY_UP:
            self.direction = key
        elif key == curses.KEY_LEFT and self.direction != curses.KEY_RIGHT:
            self.direction = key
        elif key == curses.KEY_RIGHT and self.direction != curses.KEY_LEFT:
            self.direction = key

        return True

    def update(self):
        """Update game state"""
        if self.game_over:
            return

        # Get current head position
        head_y, head_x = self.snake[0]

        # Calculate new head position based on direction
        if self.direction == curses.KEY_UP:
            new_head = (head_y - 1, head_x)
        elif self.direction == curses.KEY_DOWN:
            new_head = (head_y + 1, head_x)
        elif self.direction == curses.KEY_LEFT:
            new_head = (head_y, head_x - 1)
        elif self.direction == curses.KEY_RIGHT:
            new_head = (head_y, head_x + 1)

        # Check wall collision
        if (new_head[0] <= 0 or new_head[0] >= self.height - 1 or
            new_head[1] <= 0 or new_head[1] >= self.width - 1):
            self.game_over = True
            return

        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return

        # Add new head
        self.snake.appendleft(new_head)

        # Check if food eaten
        if new_head == self.food:
            self.score += 10
            self.spawn_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()

    def draw(self):
        """Draw game state"""
        self.stdscr.clear()

        # Draw border
        for y in range(self.height):
            self.stdscr.addstr(y, 0, '#')
            self.stdscr.addstr(y, self.width - 1, '#')
        for x in range(self.width):
            self.stdscr.addstr(0, x, '#')
            self.stdscr.addstr(self.height - 1, x, '#')

        # Draw snake
        for i, (y, x) in enumerate(self.snake):
            if i == 0:
                self.stdscr.addstr(y, x, 'O')  # Head
            else:
                self.stdscr.addstr(y, x, 'o')  # Body

        # Draw food
        self.stdscr.addstr(self.food[0], self.food[1], '*')

        # Draw score
        score_text = f'Score: {self.score} | Press q to quit'
        self.stdscr.addstr(self.height, 0, score_text)

        # Draw game over message
        if self.game_over:
            msg = f'GAME OVER! Final Score: {self.score} | Press r to restart or q to quit'
            y = self.height // 2
            x = max(0, (self.width - len(msg)) // 2)
            self.stdscr.addstr(y, x, msg, curses.A_BOLD)

        self.stdscr.refresh()

    def run(self):
        """Main game loop"""
        while True:
            if not self.handle_input():
                break

            # Check for restart
            key = self.stdscr.getch()
            if self.game_over and key == ord('r'):
                self.reset_game()

            self.update()
            self.draw()

def main(stdscr):
    game = SnakeGame(stdscr)
    game.run()

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
