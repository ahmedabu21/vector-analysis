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
z_label = Label(master=UI, text='Enter Z-Component: ')
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
magnitude_label.grid(row=5, column=0, columnspan=6, pady=5)

class Vector:
    def __init__(self):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.vector_plot = self.fig.add_subplot(111, projection='3d')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=UI)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=6, pady=20)    # Move plot below inputs
    def display(self):
        try:    
          self.x_component = float(x_entry.get())
          self.y_component = float(y_entry.get())
          self.z_component = float(z_entry.get())
        except ValueError:
          print("Invalid input! Please enter numeric values.")
          return

        self.vector_plot.clear()
        fig = plt.figure()
        octants = [
            (1, 1, 1), (-1, 1, 1), (1, -1, 1), (1, 1, -1),
            (-1, -1, 1), (-1, 1, -1), (1, -1, -1), (-1, -1, -1)
        ]
        for sign_x, sign_y, sign_z in octants:
            num_points = int(abs(self.x_component) + abs(self.y_component) + abs(self.z_component))
           
            x = np.linspace(0, sign_x * self.x_component, 1)
            y = np.linspace(0, sign_y * self.y_component, 1)
            z = np.linspace(0, sign_z * self.z_component, 1)
            self.vector_plot.plot(x, y, z, marker='o')
            



        # YZ plane (x = 0)
        X = np.linspace(-max(abs(self.x_component), abs(self.y_component)), max(abs(self.x_component), abs(self.y_component)), 10)
        Y, Z = np.meshgrid(X, X)
        self.vector_plot.plot_surface(np.zeros_like(Y), Y, Z, color='grey', alpha=.3)  # Adjusted alpha

        # XZ plane (y = 0)
        Y = np.linspace(-max(abs(self.x_component), abs(self.y_component)), max(abs(self.x_component), abs(self.y_component)), 10)
        X, Z = np.meshgrid(Y, Y)
        self.vector_plot.plot_surface(X, np.zeros_like(X), Z, color='grey', alpha=0.3 )  # Adjusted alpha

        # XY plane (z = 0)
        Z = np.linspace(-max(abs(self.x_component), abs(self.z_component)), max(abs(self.x_component), abs(self.z_component)), 10)
        X, Y = np.meshgrid(Z, Z)
        self.vector_plot.plot_surface(X, Y, np.zeros_like(X), color='grey', alpha=0.3)  # Adjusted alpha

        
#planes 

        max_value = max(abs(self.x_component), abs(self.y_component), abs(self.z_component))
        self.vector_plot.plot([-max_value, max_value], [0, 0], [0, 0], color='black', lw=2, label='X-Axis')

        self.vector_plot.plot([0, 0], [-max_value, max_value], [0, 0], color='blue', lw=2, label='Y-Axis')

        self.vector_plot.plot([0, 0], [0, 0], [-max_value, max_value], color='red', lw=2, label='Z-Axis')
        
        
        
        
        
        num_points=10* int(abs(self.x_component) +abs(self.y_component ) + abs(self.z_component))
        
        x = np.linspace(0, self.x_component, num_points)
        y = np.linspace(0, self.y_component, num_points)
        z = np.linspace(0, self.z_component, num_points)
        self.vector_plot.plot(x,y,z, c='r', marker='o')
        
        x2 = np.linspace(0, -self.x_component, num_points)
        y2 = np.linspace(0, -self.y_component, num_points)
        z2 = np.linspace(0, -self.z_component, num_points)
        
        
        self.vector_plot.plot(x2,y2,z2, c='b', marker='o', label='-vector')
        
        
        
        
        

        
        grid_range = np.linspace(-max_value, max_value, 10)

        # Set the grid lines for each axis to extend into all octants
        self.vector_plot.set_xticks(grid_range)
        self.vector_plot.set_yticks(grid_range)
        self.vector_plot.set_zticks(grid_range)

        # Display grid lines
        self.vector_plot.grid(True, linestyle='--', alpha=0.5)

        self.vector_plot.set_xlabel('X Component')
        self.vector_plot.set_ylabel('Y Component')
        self.vector_plot.set_zlabel('Z Component')
        self.vector_plot.legend()
        self.canvas.draw()

        magnitude = np.sqrt(self.x_component**2 + self.y_component**2 + self.z_component**2)
        magnitude_label.config(text=f'Magnitude: {magnitude:.2f}')
    def addVectors(vector1,vector2):
        newX = vector1.xCom + vector2.xCom
        newY= vector1.yCom + vector2.yCom
        newZ = vector1.zCom + vector2.zCom
        return Vector(newX, newY, newZ)

        
       
vector_instance = Vector()

plot_button = Button(master=UI, text="Plot", height=2, width=10, command=vector_instance.display)
plot_button.grid(row=1, column=2,  pady=20)  
addButt = Button(master=UI,text="Add",height=2, width=10, command=vector_instance.addVectors)
addButt.grid(row=2, column=0, padx=5, pady=5)
subButt = Button(master=UI,text="Subtract",height=2, width=10)#add command
subButt.grid(row=2, column=1, padx=5, pady=5)
dotButt = Button(master=UI,text="Dot Product",height=2, width=10)
dotButt.grid(row=2, column=2, padx=5, pady=5)
crossButt = Button(master=UI,text="Cross Product",height=2, width=10)
crossButt.grid(row=2, column=3, padx=5, pady=5)



UI.mainloop()

    