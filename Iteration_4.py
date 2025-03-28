#Created by Karan, Ahmed, Oliee | 2025
#Iteration #4
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 


UI = Tk()
UI.title('Vector Analysis!')
UI.geometry("500x500")
plot_button = Button(master=UI, height=5, width=20, text = "plot")
x_label= Label(master=UI, text='Enter X-Component: ')
y_label = Label(master=UI, text='Enter Y-Component: ')
z_label = Label(master=UI, text='Enter Z Component: ')
x_entry = Entry(UI, width=10, borderwidth=3)
y_entry = Entry(UI, width=10, borderwidth=3)
z_entry = Entry(UI, width=10, borderwidth=3)
x_label.grid(row=0, column=0, padx=5)
x_entry.grid(row=0, column=1, padx=5)
y_label.grid(row=0, column=2, padx=5)
y_entry.grid(row=0, column=3, padx=5)
z_label.grid(row=0, column=4, padx=5)
z_entry.grid(row=0, column=5, padx=5)



class Vector:
    def __init__(self):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.vector_plot = self.fig.add_subplot(111, projection='3d')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=UI)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=6, pady=20)    # Move plot below inputs

    def display(self):
        try:
            x_component = float(x_entry.get())
            y_component = float(y_entry.get())
            z_component = float(z_entry.get())
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

    # Clear previous figure memory usage
        plt.close('all')

    # Clear the previous plot
        self.vector_plot.clear()
    
    # Plot the vector
        self.vector_plot.quiver(0, 0, 0, x_component, y_component, z_component, color='r', arrow_length_ratio=0.1)
    
    # Label axes
        self.vector_plot.set_xlabel('X Component')
        self.vector_plot.set_ylabel('Y Component')
        self.vector_plot.set_zlabel('Z Component')

    # Redraw the canvas
        self.canvas.draw()

        
       
vector_instance = Vector()
plot_button = Button(master=UI, text="Plot", height=2, width=10, command=vector_instance.display)
plot_button.grid(row=1, column=0, columnspan=6, pady=20)  




UI.mainloop()

    



# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z


#     @classmethod
#     def from_magnitude_direction(cls, magnitude, direction):

#         dx, dy, dz = direction
#         norm = np.sqrt(dx**2 + dy**2 + dz**2)
#         unit_vector = (dx / norm, dy / norm, dz / norm)
#         x, y, z = magnitude * np.array(unit_vector)
#         return cls(x, y, z)

   

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
    