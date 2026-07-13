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
        
        # Move to requested location
        x = x + self.x_orig
        y = y + self.y_orig

        self.x = x
        self.y = y
        self.spiral_generated = True
        self.num_points = num_points

        return self.x, self.y
    

    def get_spiral(self):
        if self.spiral_generated == False:
            raise Exception("Spiral not generated!")
        
        return self.x, self.y