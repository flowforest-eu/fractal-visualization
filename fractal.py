import numpy as np
import matplotlib.pyplot as plt
from curve import Curve


def generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, angle_deg=0, mirror=False, t=0):
    # Polar definitions
    r = np.cos(t)
    theta = np.tan(t) - t
    
    # Convert to base Cartesian coordinates
    x_base = r * np.cos(theta)
    y_base = r * np.sin(theta)

    # Substract vector (1,0), which is position of tractrix at t=0. So then t=0 is at (0,0).
    x_base = x_base - 1

    # Scale by a
    x_base = scale * x_base
    y_base = scale * y_base

    # Rotate by 90 degrees (pi/2) to orient it like an upright question mark/fern
    angle_rad = np.radians(angle_deg)
    rotation_angle = np.pi / 2 - angle_rad
    x = x_base * np.cos(rotation_angle) - y_base * np.sin(rotation_angle)
    y = x_base * np.sin(rotation_angle) + y_base * np.cos(rotation_angle)

    if mirror == True:
        x = -x

    # Move to requested location
    x = x + x_orig
    y = y + y_orig

    return x, y


# TODO add mirror?
def get_direction_angle(t, angle_deg=0, mirror=False):
    # Using small epsilon for finite difference to get tangent
    eps = 1e-5
    def get_coords(time):
        t_val = time
        r = np.cos(t_val)
        theta = np.tan(t_val) - t_val
        return r * np.cos(theta), r * np.sin(theta)
    
    x1, y1 = get_coords(t)
    x2, y2 = get_coords(t + eps)
    
    dx = (x2 - x1) / eps
    dy = (y2 - y1) / eps
    
    # Standard angle in radians (East = 0)
    alpha = np.arctan2(dy, dx)
    
    # Convert to degrees and shift so South = 0, East = 90
    phi = np.degrees(alpha) + 90
    
    return phi % 360


# Generate the coordinates
curve1 = Curve(x_orig=0, y_orig=0, scale=1.0, angle_deg=0, mirror=False)
x, y = curve1.generate_spiral()

# Plot the curve
plt.figure(figsize=(6, 8), dpi=100)
plt.plot(x, y, color='black', linewidth=2, solid_capstyle='round')

# Second curve
# TODO: generate_tractrix_data_at_point(curve1, t=1.35)
x1, y1 = generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, t=1.35)
angle_deg = get_direction_angle(t=1.35, angle_deg=0, mirror=False)
# TODO: curve1.branch_at_point(...)
curve2 = Curve(x_orig=x1, y_orig=y1, mirror=True, angle_deg = angle_deg, scale=1.0)
x, y = curve2.generate_spiral()
plt.plot(x, y, color='black', linewidth=2, solid_capstyle='round')

### Third curve
# TODO: generate_tractrix_data_at_point(curve2, t=1.4)
xn1, yn1 = generate_tractrix_point(scale=1.0, x_orig=x1, y_orig=y1, mirror=True, angle_deg=angle_deg, t=1.4)
angle_deg_new = get_direction_angle(t=1.4, angle_deg=angle_deg, mirror=True)
# TODO: curve1.branch_at_point(...)
curve3 = Curve(x_orig=xn1, y_orig=yn1, mirror=False, angle_deg=angle_deg_new, scale=1.0)
x, y = curve3.generate_spiral()
plt.plot(x, y, color='black', linewidth=2, solid_capstyle='round')

# Plot origin
plt.plot(0, 0, 'go', markersize=3)

# Plot some points
pointx, pointy = generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, t=1.27)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, t=1.29)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, t=1.31)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, t=1.33)
plt.plot(pointx, pointy, 'bo', markersize=6)
pointx, pointy = generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, t=1.35)
plt.plot(pointx, pointy, 'bo', markersize=6)
pointx, pointy = generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, t=1.37)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, t=1.38)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, t=1.39)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, t=1.4)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, t=1.41)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, t=1.42)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(scale=1.0, x_orig=0, y_orig=0, t=1.43)
plt.plot(pointx, pointy, 'ro', markersize=6)

# Format the image to be a perfect base for the fractal mapping
plt.axis('equal')
plt.axis('off')
plt.tight_layout()

# Save the clean asset
plt.savefig("tractrix_spiral_base.png", bbox_inches='tight', transparent=True)
plt.show()