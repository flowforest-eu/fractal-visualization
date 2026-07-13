import numpy as np
import matplotlib.pyplot as plt
from curve import Curve


# Generate the coordinates
curve1 = Curve(x_orig=0, y_orig=0, scale=1.0, angle_deg=0, mirror=False)
x, y = curve1.generate_spiral()

# Plot the curve
plt.figure(figsize=(6, 8), dpi=100)
plt.plot(x, y, color='black', linewidth=2, solid_capstyle='round')

# Second curve
curve2 = curve1.branch_at_point(t=1.35, scale=1.0, mirror=True)
x, y = curve2.generate_spiral()
plt.plot(x, y, color='black', linewidth=2, solid_capstyle='round')

# ### Third curve
curve3 = curve2.branch_at_point(t=1.4, mirror=False, scale=1.0)
x, y = curve3.generate_spiral()
plt.plot(x, y, color='black', linewidth=2, solid_capstyle='round')

# Plot origin
plt.plot(0, 0, 'go', markersize=3)

# Plot some points
pointx, pointy = curve1.calculate_point(t=1.27)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = curve1.calculate_point(t=1.29)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = curve1.calculate_point(t=1.31)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = curve1.calculate_point(t=1.33)
plt.plot(pointx, pointy, 'bo', markersize=6)
pointx, pointy = curve1.calculate_point(t=1.35)
plt.plot(pointx, pointy, 'bo', markersize=6)
pointx, pointy = curve1.calculate_point(t=1.37)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = curve1.calculate_point(t=1.38)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = curve1.calculate_point(t=1.39)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = curve1.calculate_point(t=1.4)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = curve1.calculate_point(t=1.41)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = curve1.calculate_point(t=1.42)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = curve1.calculate_point(t=1.43)
plt.plot(pointx, pointy, 'ro', markersize=6)

# Format the image to be a perfect base for the fractal mapping
plt.axis('equal')
plt.axis('off')
plt.tight_layout()

# Save the clean asset
plt.savefig("tractrix_spiral_base.png", bbox_inches='tight', transparent=True)
plt.show()