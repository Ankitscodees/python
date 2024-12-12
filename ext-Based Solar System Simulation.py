import math
import time
import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def simulate_solar_system():
    """Simulates a solar system with planets orbiting around the sun."""
    width, height = 40, 20  # Dimensions of the display
    sun_x, sun_y = width // 2, height // 2  # Position of the sun
    planet_orbits = [4, 7, 10, 13]  # Distances of planets from the sun
    angles = [0, 0, 0, 0]  # Initial angles of the planets

    while True:
        clear_screen()
        # Create an empty screen
        screen = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Place the sun
        screen[sun_y][sun_x] = '*'
        
        # Update planet positions
        for i, orbit in enumerate(planet_orbits):
            angles[i] += (i + 1) * 0.1  # Adjust the speed of rotation
            x = sun_x + int(orbit * math.cos(angles[i]))
            y = sun_y + int(orbit * math.sin(angles[i]))
            if 0 <= x < width and 0 <= y < height:
                screen[y][x] = 'O'
        
        # Print the screen
        for row in screen:
            print(''.join(row))
        
        time.sleep(0.1)

# Run the simulation
simulate_solar_system()
