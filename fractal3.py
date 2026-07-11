import numpy as np
import matplotlib.pyplot as plt

def generate_tractrix_spiral(a=1.0, x_orig=0, y_orig=0, angle_deg=0, mirror=False, num_points=5000):
    # Parameter t runs from 0 close to pi/2 to avoid tan(pi/2) division by zero
    t = np.linspace(0, np.pi/2 - 0.06, num_points)
    
    # Polar definitions
    r = a * np.cos(t)
    theta = np.tan(t) - t
    
    # Convert to base Cartesian coordinates
    x_base = r * np.cos(theta)
    y_base = r * np.sin(theta)

    # Move to shape origin
    shift_x = x_base[0]
    shift_y = y_base[0]

    x_base = x_base - shift_x
    y_base = y_base - shift_y

    # Rotate by 90 degrees (pi/2) to orient it like an upright question mark/fern; then rotate by angle
    angle_rad = np.radians(angle_deg)
    rotation_angle = np.pi / 2 - angle_rad
    x = x_base * np.cos(rotation_angle) - y_base * np.sin(rotation_angle)
    y = x_base * np.sin(rotation_angle) + y_base * np.cos(rotation_angle)

    if mirror == True:
        x = x[0] + (x[0] - x)
    
    # Move to correct location
    x = x + x_orig
    y = y + y_orig

    return x, y


# TODO angle_deg, mirror
def generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, angle_deg=0, mirror=False, t=0):
    # Polar definitions
    r = a * np.cos(t)
    theta = np.tan(t) - t
    
    # Convert to base Cartesian coordinates
    x_base = r * np.cos(theta)
    y_base = r * np.sin(theta)

    # Calculate origin at t=0
    r0 = a * np.cos(0)
    theta0 = np.tan(0)
    x0 = r0 * np.cos(theta0)
    y0 = r0 * np.sin(theta0)

    # Move to shape origin
    x_base = x_base - x0
    y_base = y_base - y0

    # Rotate by 90 degrees (pi/2) to orient it like an upright question mark/fern
    angle_rad = np.radians(angle_deg)

    rotation_angle = np.pi / 2 - angle_rad
    x = x_base * np.cos(rotation_angle) - y_base * np.sin(rotation_angle)
    y = x_base * np.sin(rotation_angle) + y_base * np.cos(rotation_angle)

    if mirror == True:
        x = x[0] + (x[0] - x)

    # Move to correct location
    x = x + x_orig
    y = y + y_orig

    return x, y


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
x, y = generate_tractrix_spiral(a=1.0, x_orig=0, y_orig=0, angle_deg=0)

# Plot the curve
# plt.figure(figsize=(6, 8), dpi=100)
plt.plot(x, y, color='black', linewidth=2, solid_capstyle='round')

print()

# Second curve
x0, y0 = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=0)
# x1, y1 = generate_tractrix_point(a=1.0, x0=0, y0=0, t=1.35)
angle_deg = get_direction_angle(t=1.41, angle_deg=0, mirror=False)
x1, y1 = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=1.41)
x, y = generate_tractrix_spiral(a=1.0, x_orig=x1-x0, y_orig=y1-y0, mirror=True, angle_deg=angle_deg)
plt.plot(x, y, color='black', linewidth=2, solid_capstyle='round')

# Plot origin
plt.plot(0, 0, 'go', markersize=3)

# Plot some points
pointx, pointy = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=1.27)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=1.29)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=1.31)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=1.33)
plt.plot(pointx, pointy, 'bo', markersize=6)
pointx, pointy = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=1.35)
plt.plot(pointx, pointy, 'bo', markersize=6)
pointx, pointy = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=1.37)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=1.38)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=1.39)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=1.4)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=1.41)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=1.42)
plt.plot(pointx, pointy, 'ro', markersize=6)
pointx, pointy = generate_tractrix_point(a=1.0, x_orig=0, y_orig=0, t=1.43)
plt.plot(pointx, pointy, 'ro', markersize=6)

# Format the image to be a perfect base for the fractal mapping
plt.axis('equal')
plt.axis('off')
plt.tight_layout()

# Save the clean asset
plt.savefig("tractrix_spiral_base.png", bbox_inches='tight', transparent=True)
plt.show()