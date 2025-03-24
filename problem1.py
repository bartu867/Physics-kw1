import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Gravity (m/s²)
v0 = 20   # Initial velocity (m/s)

# Define angles (0° - 90°)
angles = np.linspace(0, 90, 100)
radians = np.radians(angles)

# Compute the projectile range
range_values = (v0**2 * np.sin(2 * radians)) / g

# Plot the graph
plt.figure(figsize=(8, 5))
plt.plot(angles, range_values, label="Range")
plt.axvline(45, color="red", linestyle="--", label="Optimal Angle (45°)")
plt.xlabel("Launch Angle (°)")
plt.ylabel("Range (m)")
plt.title("Projectile Range vs. Launch Angle")
plt.legend()
plt.grid()

# Save and show
plt.savefig("output_graph.png")
plt.show()
