#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # Generating random mine locations using a set for fast lookups
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]  # Display grid
        self.revealed = [[False for _ in range(width)] for _ in range(height)]  # Revealed cells tracker

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(f'{i:2}' for i in range(self.width)))  # Print column headers
        for y in range(self.height):
            print(f'{y:2} ', end='')  # Print row number for each row
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')  # Mine
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')  # Number of mines or empty
                else:
                    print('.', end=' ')  # Unrevealed cells
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # If it's a mine, game over
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:  # If no nearby mines, recursively reveal neighbors
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()  # Show the board at each step
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                # Ensure the coordinates are within valid ranges
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Invalid coordinates. Please try again.")
                    continue

                if not self.reveal(x, y):  # If a mine is hit
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                # Check if all non-mine cells are revealed (i.e., the game is won)
                if self.check_win():
                    self.print_board(reveal=True)
                    print("Congratulations! You cleared the board!")
                    break

            except ValueError:
                print("Invalid input. Please enter valid numbers.")

    def check_win(self):
        # Check if all non-mine cells have been revealed
        for y in range(self.height):
            for x in range(self.width):
                if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                    return False
        return True

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
