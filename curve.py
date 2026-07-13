import numpy as np


class Curve:
    """
    A class representing a tractrix shape

    Attributes:
        x_orig (float): origin point (x-axis)
        y_orig (float): origin point (y-axis)
        scale (float): scale of the shape, where 1.0 is "original size"
        angle_deg (float): angle in degrees between vector pointing south and stem of the shape (measured clockwise). if angle_deg = 0, shape will start to grow to south initially.
        mirror (bool): whether to mirror the shape along y-axis (vertically)
    """
    def __init__(self, x_orig, y_orig, scale, angle_deg, mirror):
        self.x_orig = x_orig
        self.y_orig = y_orig
        self.scale = scale
        self.angle_deg = angle_deg
        self.mirror = mirror
        self.spiral_generated = False
        self.num_points = -1
        self.x = []
        self.y = []


    def generate_spiral(self, num_points=5000):
        # Parameter t runs from 0 close to pi/2 to avoid tan(pi/2) division by zero
        t = np.linspace(0, np.pi/2 - 0.06, num_points)
        
        # Polar definitions
        r = np.cos(t)
        theta = np.tan(t) - t
        
        # Convert to base Cartesian coordinates
        x_base = r * np.cos(theta)
        y_base = r * np.sin(theta)

        # Substract vector (1,0), which is position of tractrix at t=0. So then t=0 is at (0,0).
        x_base = x_base - 1

        # Scale
        x_base = self.scale * x_base
        y_base = self.scale * y_base

        # Rotate by 90 degrees (pi/2) to orient it like an upright question mark/fern
        x_rotated = x_base * np.cos(np.pi / 2) - y_base * np.sin(np.pi / 2)
        y_rotated = x_base * np.sin(np.pi / 2) + y_base * np.cos(np.pi / 2)

        # if requested, add mirroring
        if self.mirror == True:
            x_rotated = -x_rotated

        # Turn by requested angle (clockwise)
        angle_rad = np.radians(-self.angle_deg)
        x = x_rotated * np.cos(angle_rad) - y_rotated * np.sin(angle_rad)
        y = x_rotated * np.sin(angle_rad) + y_rotated * np.cos(angle_rad)
        
        # Move to correct location
        x = x + self.x_orig
        y = y + self.y_orig

        self.x = x
        self.y = y
        self.spiral_generated = True
        self.num_points = num_points

        return self.x, self.y
    

    def calculate_point(self, t):
        # Polar definitions
        r = np.cos(t)
        theta = np.tan(t) - t
        
        # Convert to base Cartesian coordinates
        x_base = r * np.cos(theta)
        y_base = r * np.sin(theta)

        # Substract vector (1,0), which is position of tractrix at t=0. So then t=0 is at (0,0).
        x_base = x_base - 1

        # Scale by a
        x_base = self.scale * x_base
        y_base = self.scale * y_base
        
        # Rotate by 90 degrees (pi/2) to orient it like an upright question mark/fern
        x_rotated = x_base * np.cos(np.pi / 2) - y_base * np.sin(np.pi / 2)
        y_rotated = x_base * np.sin(np.pi / 2) + y_base * np.cos(np.pi / 2)

        # if requested, add mirroring
        if self.mirror == True:
            x_rotated = -x_rotated

        # Turn by requested angle (clockwise)
        angle_rad = np.radians(-self.angle_deg)
        x = x_rotated * np.cos(angle_rad) - y_rotated * np.sin(angle_rad)
        y = x_rotated * np.sin(angle_rad) + y_rotated * np.cos(angle_rad)
        
        # Move to correct location
        x = x + self.x_orig
        y = y + self.y_orig

        return x, y


    def get_direction_angle(self, t):
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
        
        # Standard angle in radians (East = 0, counting counter-clockwise)
        alpha = np.arctan2(dy, dx)
        
        # Convert to degrees
        phi = np.degrees(alpha)

        # Inverse (East = 0, counting clockwise)
        phi = -phi
        
        # shift so South = 0, West = 90   
        phi = phi - 90

        # Consider mirroring
        if self.mirror:
            phi = -phi

        # Consider original rotation of the shape
        phi = phi + self.angle_deg

        return phi % 360


    def get_spiral(self):
        if self.spiral_generated == False:
            raise Exception("Spiral not generated!")
        
        return self.x, self.y
    

    def branch_at_point(self, t, scale, mirror):
        # find origin point for the new curve
        x_new, y_new = self.calculate_point(t)
        new_angle_deg = self.get_direction_angle(t)
        new_curve = Curve(x_orig=x_new, y_orig=y_new, mirror=mirror, angle_deg = new_angle_deg, scale=scale)
        return new_curve
