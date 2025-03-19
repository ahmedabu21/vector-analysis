#Created by Karan, Ahmed, Oliee | 2025
#Iteration #4
import numpy as np


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
   

    @classmethod
    def from_magnitude_direction(cls, magnitude, direction):

        dx, dy, dz = direction
        norm = np.sqrt(dx**2 + dy**2 + dz**2)
        unit_vector = (dx / norm, dy / norm, dz / norm)
        x, y, z = magnitude * np.array(unit_vector)
        return cls(x, y, z)

   

    @staticmethod
    def magnitude_direction(v):
        magnitude = np.sqrt(v.x**2 + v.y**2 + v.z**2)
        direction = (v.x / magnitude, v.y / magnitude, v.z / magnitude)
        return magnitude, direction

   

    @staticmethod
    def add(v1, v2):
        return Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)

    @staticmethod
    def subtract(v1, v2):
        return Vector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)

   

    @staticmethod
    def dot(v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

   

    @staticmethod
    def cross(v1, v2):
        cross_product = np.cross([v1.x, v1.y, v1.z], [v2.x, v2.y, v2.z])
        return Vector(*cross_product)

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
if __name__ == "__main__":

    mag = float(input("Enter magnitude: "))
    dx = float(input("Enter direction x component: "))
    dy = float(input("Enter direction y component: "))
    dz = float(input("Enter direction z component: "))
    
    v1 = Vector.from_magnitude_direction(mag, (dx, dy, dz))
    print(f"Vector: {v1}")

   

    mag_calc, direction_v1 = v1.magnitude_direction(v1)
    print(f"Computed magnitude: {mag_calc:.3f}")
    print(f"Computed direction: {direction_v1}")

    v2 = Vector(1, 2, 3)
    print(f"Vector addition: {Vector.add(v1, v2)}")
    print(f"Vector subtraction: {Vector.subtract(v1, v2)}")
    print(f"Dot product: {Vector.dot(v1, v2)}")
    print(f"Cross product: {Vector.cross(v1, v2)}")
