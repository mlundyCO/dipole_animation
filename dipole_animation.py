import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define constants
k = 1
omega = 1

# Step 1: Define the implicit function f(r, theta, t) = C
def field_line_function(r, theta, t):
    return (np.sin(k*r - omega*t) + np.cos(k*r - omega*t)/(k*r))*(np.sin(theta))**2

# Step 2: Create a grid of r and theta values
r = np.linspace(0.1, 10, 100)  # Adjust range as needed
theta = np.linspace(0, 2 * np.pi, 100)  # Full circle in radians
R, Theta = np.meshgrid(r, theta)

# Step 3: Prepare the figure and axis for animation
fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Electric Field Lines Animation')
ax.set_aspect('equal')
ax.grid(True)

# Step 4: Define the function to update the plot for each time step t
def update(t):
    ax.clear()  # Clear previous plot
    Z = field_line_function(R, Theta, t)  # Compute new field line data
    contour_levels = np.linspace(-5, 5, 50)  # Define C values (contour levels)
    cp = ax.contour(R * np.cos(Theta), R * np.sin(Theta), Z, levels=contour_levels)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'Electric Field Lines at t = {t:.2f}')
    ax.grid(True)
    ax.set_aspect('equal')

# Step 5: Create the animation
# Define the range of t values for the animation
t_values = np.linspace(0, 50, 1000)  # Adjust t range and number of frames

# Use FuncAnimation to create the animation
ani = FuncAnimation(fig, update, frames=t_values, interval=100)

# Step 6: Show the animation
plt.show()

# If you want to save the animation to a file (e.g., GIF or MP4), you can do so like this:
# ani.save('electric_field_lines_animation.gif', writer='imagemagick', fps=10)
# ani.save('electric_field_lines_animation.mp4', writer='ffmpeg', fps=10)
