import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

UI = Tk()
UI.title('Vector Analysis!')
UI.geometry("600x600")

# UI Components
x_label = Label(UI, text='Enter X-Component: ')
y_label = Label(UI, text='Enter Y-Component: ')
z_label = Label(UI, text='Enter Z-Component: ')
x_entry = Entry(UI, width=10, borderwidth=3)
y_entry = Entry(UI, width=10, borderwidth=3)
z_entry = Entry(UI, width=10, borderwidth=3)

x_label.grid(row=0, column=0, padx=5)
x_entry.grid(row=0, column=1, padx=5)
y_label.grid(row=0, column=2, padx=5)
y_entry.grid(row=0, column=3, padx=5)
z_label.grid(row=0, column=4, padx=5)
z_entry.grid(row=0, column=5, padx=5)

magnitude_label = Label(UI, text='Magnitude: N/A', font=("Arial", 12))
magnitude_label.grid(row=2, column=0, columnspan=6, pady=5)

class Vector:
    def __init__(self):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.vector_plot = self.fig.add_subplot(111, projection='3d')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=UI)
        self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=6, pady=20)  

    def display(self):
        try:    
            self.x_component = float(x_entry.get())
            self.y_component = float(y_entry.get())
            self.z_component = float(z_entry.get())
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        self.vector_plot.clear()  # Clear the previous plot instead of creating a new figure

        max_value = max(abs(self.x_component), abs(self.y_component), abs(self.z_component))

        # Draw Axes
        self.vector_plot.plot([-max_value, max_value], [0, 0], [0, 0], color='black', lw=2, label='X-Axis')
        self.vector_plot.plot([0, 0], [-max_value, max_value], [0, 0], color='blue', lw=2, label='Y-Axis')
        self.vector_plot.plot([0, 0], [0, 0], [-max_value, max_value], color='red', lw=2, label='Z-Axis')

        # Plot Vector
        num_points = int(abs(self.x_component) + abs(self.y_component) + abs(self.z_component))
        x = np.linspace(0, self.x_component, num_points)
        y = np.linspace(0, self.y_component, num_points)
        z = np.linspace(0, self.z_component, num_points)
        self.vector_plot.plot(x, y, z, c='r', marker='o', label='Vector')

        # XY, YZ, and XZ Planes
        X = np.linspace(-max_value, max_value, 10)
        Y, Z = np.meshgrid(X, X)
        self.vector_plot.plot_surface(np.zeros_like(Y), Y, Z, color='grey', alpha=0.3)
        self.vector_plot.plot_surface(X, np.zeros_like(X), Z, color='grey', alpha=0.3)
        self.vector_plot.plot_surface(X, Y, np.zeros_like(X), color='grey', alpha=0.3)

        # Set Labels
        self.vector_plot.set_xlabel('X Component')
        self.vector_plot.set_ylabel('Y Component')
        self.vector_plot.set_zlabel('Z Component')
        self.vector_plot.legend()

        # Update Canvas
        self.canvas.draw()

        # Update Magnitude Label
        self.magnitude()

    def magnitude(self):
        magnitude = np.sqrt(self.x_component**2 + self.y_component**2 + self.z_component**2)
        magnitude_label.config(text=f'Magnitude: {magnitude:.2f}')

vector_instance = Vector()

plot_button = Button(master=UI, text="Plot", height=2, width=10, command=vector_instance.display)
plot_button.grid(row=1, column=0, columnspan=6, pady=10)

UI.mainloop()


# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z


    # @classmethod
    # def from_magnitude_direction(cls, magnitude, direction):

    #     dx, dy, dz = direction
    #     norm = np.sqrt(dx**2 + dy**2 + dz**2)
    #     unit_vector = (dx / norm, dy / norm, dz / norm)
    #     x, y, z = magnitude * np.array(unit_vector)
    #     return cls(x, y, z)

   

#     @staticmethod
#     def magnitude_direction(v):
#         magnitude = np.sqrt(v.x**2 + v.y**2 + v.z**2)
#         direction = (v.x / magnitude, v.y / magnitude, v.z / magnitude)
#         return magnitude, direction

   

#     @staticmethod
#     def add(v1, v2):
#         return Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)

#     @staticmethod
#     def subtract(v1, v2):
#         return Vector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)

   

#     @staticmethod
#     def dot(v1, v2):
#         return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

   

#     @staticmethod
#     def cross(v1, v2):
#         cross_product = np.cross([v1.x, v1.y, v1.z], [v2.x, v2.y, v2.z])
#         return Vector(*cross_product)

#     def __repr__(self):
#         return f"Vector({self.x}, {self.y}, {self.z})"
    
# if __name__ == "__main__":

#     mag = float(input("Enter magnitude: "))
#     dx = float(input("Enter direction x component: "))
#     dy = float(input("Enter direction y component: "))
#     dz = float(input("Enter direction z component: "))
    
#     v1 = Vector.from_magnitude_direction(mag, (dx, dy, dz))
#     print(f"Vector: {v1}")

   

#     mag_calc, direction_v1 = v1.magnitude_direction(v1)
#     print(f"Computed magnitude: {mag_calc:.3f}")
#     print(f"Computed direction: {direction_v1}")

#     v2 = Vector(1, 2, 3)
#     print(f"Vector addition: {Vector.add(v1, v2)}")
#     print(f"Vector subtraction: {Vector.subtract(v1, v2)}")
#     print(f"Dot product: {Vector.dot(v1, v2)}")
#     print(f"Cross product: {Vector.cross(v1, v2)}")
    