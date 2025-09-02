# player.py

class Player:
    def __init__(self, x=0, y=0):
        # Initialize player position
        self.x = x
        self.y = y
        # Indicates whether player is painting
        self.painting = False

    def move(self, dx, dy, grid_size):
        # Move player by dx/dy within grid bounds
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < grid_size:
            self.x = new_x
        if 0 <= new_y < grid_size:
            self.y = new_y

    def toggle_paint(self):
        # Toggle painting state
        self.painting = not self.painting
