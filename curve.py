import numpy as np


class Curve:
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

        # Rotate by 90 degrees (pi/2) to orient it like an upright question mark/fern; then rotate by angle
        angle_rad = np.radians(self.angle_deg)
        rotation_angle = np.pi / 2 - angle_rad
        x = x_base * np.cos(rotation_angle) - y_base * np.sin(rotation_angle)
        y = x_base * np.sin(rotation_angle) + y_base * np.cos(rotation_angle)

        if self.mirror == True:
            x = -x
        
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
        angle_rad = np.radians(self.angle_deg)
        rotation_angle = np.pi / 2 - angle_rad
        x = x_base * np.cos(rotation_angle) - y_base * np.sin(rotation_angle)
        y = x_base * np.sin(rotation_angle) + y_base * np.cos(rotation_angle)

        if self.mirror == True:
            x = -x

        # Move to correct location
        x = x + self.x_orig
        y = y + self.y_orig

        return x, y


    # TODO add mirror? remove from params here
    # TODO add angle_deg? remove from params here
    def get_direction_angle(self, t, angle_deg=0, mirror=False):
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


    def get_spiral(self):
        if self.spiral_generated == False:
            raise Exception("Spiral not generated!")
        
        return self.x, self.y
    

    def branch_at_point(self, t, scale, mirror):
        # find origin point for the new curve
        x_new, y_new = self.calculate_point(t=1.35)
        new_angle_deg = self.get_direction_angle(t=1.35, angle_deg=self.angle_deg, mirror=self.mirror)
        new_curve = Curve(x_orig=x_new, y_orig=y_new, mirror=mirror, angle_deg = new_angle_deg, scale=scale)
        return new_curve
