#Created by Karan, Ahmed, Oliee | 2025

# Import required libraries for plotting, numerical computation, and GUI
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
from tkinter import messagebox

<<<<<<< HEAD
# Initialize the Tkinter GUI window
UI = Tk() # establishes UI through tkinter library 
UI.title('Vector Analysis!') # application name
UI.geometry("570x700") # changes pizel size of UI
UI.configure(bg="#E8F6F3") # changes background color to light teal  
UI.resizable(False, False) # Disables resizing 
=======
UI = Tk() #establishes UI through tkinter library 
UI.title('Vector Analysis!') #application name
UI.geometry("570x700") #changes pizel size of UI
UI.configure(bg="#E8F6F3") #changes background color to light teal  
UI.resizable(False, False) #so when application opens it does not let you resize it 
#testing
>>>>>>> ad410158edf824bd51bc565d10966c4374be934c

# Define Vector class to handle all vector operations and 3D plotting
class Vector:
    def __init__(self):
        # Create a Matplotlib 3D figure for plotting vectors
        self.fig = Figure(figsize=(5, 4), dpi=100) #creates plot
        self.vector_plot = self.fig.add_subplot(111, projection='3d') #makes vector plot 3-D including z-axis
        
        # Embed the plot into the Tkinter GUI
        self.canvas = FigureCanvasTkAgg(self.fig, master=UI) #places figure on UI
        self.canvas.get_tk_widget().grid(row=5, column=0, columnspan=5, pady=20) # Move plot below inputs
    
    #method allowing for object vector to be passed 
    def display(self, v1, v2, result=None): 
        self.vector_plot.clear() #clears all previous inputs of vectors
        
        # Determine axis limits based on max component value
        max_value = max(
            abs(v1[0]), abs(v1[1]), abs(v1[2]),
            abs(v2[0]), abs(v2[1]), abs(v2[2])
        ) + 1
<<<<<<< HEAD
 
        # Plot reference planes (XY, YZ, XZ)
=======
 # plots the axis planes. Mostly see through
    
>>>>>>> ad410158edf824bd51bc565d10966c4374be934c
        plane_range = np.linspace(-max_value, max_value, 10)
        # YZ Plane (x = 0)
        Y, Z = np.meshgrid(plane_range, plane_range)
        self.vector_plot.plot_surface(np.zeros_like(Y), Y, Z, color='grey', alpha=0.15) # YZ plane
        # XZ Plane (y = 0)
        X, Z = np.meshgrid(plane_range, plane_range)
        self.vector_plot.plot_surface(X, np.zeros_like(X), Z, color='grey', alpha=0.15) # XZ plane
        # XY Plane (z = 0)
        X, Y = np.meshgrid(plane_range, plane_range)
        self.vector_plot.plot_surface(X, Y, np.zeros_like(X), color='grey', alpha=0.15) # XY plane
        
        # Axes
        self.vector_plot.plot([-max_value, max_value], [0, 0], [0, 0], color='black', alpha=.55, lw=2)  # X-axis
        self.vector_plot.plot([0, 0], [-max_value, max_value], [0, 0], color='black', alpha=.55, lw=2)   # Y-axis
        self.vector_plot.plot([0, 0], [0, 0], [-max_value, max_value], color='black', alpha=.55, lw=2)    # Z-axis

        # Set axis limits
        self.vector_plot.set_xlim([-max_value, max_value])
        self.vector_plot.set_ylim([-max_value, max_value])
        self.vector_plot.set_zlim([-max_value, max_value])
        #plots axes 
        

        # Plot Vector A (Red)
        self.vector_plot.plot([0, v1[0]], [0, v1[1]], [0, v1[2]], color='r', linewidth=3, label="Vector A")
        # Plot Vector B (Blue)
        self.vector_plot.plot([0, v2[0]], [0, v2[1]], [0, v2[2]], color='b', linewidth=3, label="Vector B")

        # Plot result vector if provided
        if result is not None:
            self.vector_plot.plot([0, result[0]], [0, result[1]], [0, result[2]], color='g', linewidth=3, label="Resulting Vector")
        
        # Add axis labels and legend
        self.vector_plot.set_xlabel('X Axis')
        self.vector_plot.set_ylabel('Y Axis')
        self.vector_plot.set_zlabel('Z Axis')
        self.vector_plot.legend()
        self.canvas.draw()
<<<<<<< HEAD

    # Method to fetch vector inputs from the UI and return as lists
=======
#updates vectors using user inputs 
>>>>>>> ad410158edf824bd51bc565d10966c4374be934c
    def update_vectors(self):
        # obtain vector from Entry widgets and converts them into lists
        try:
            v1 = [float(x_entry1.get()), float(y_entry1.get()), float(z_entry1.get())]
            v2 = [float(x_entry2.get()), float(y_entry2.get()), float(z_entry2.get())]
            self.display(v1, v2) # Display the input vectors on the plot
            return v1, v2
        #error handling 
        except ValueError:
<<<<<<< HEAD
            messagebox.showinfo(text="Invalid Input! Enter numeric values.")# Show error message if input is invalid
=======
            messagebox.showinfo(text="Invalid Input! Enter numeric values.")# ensures correct data type
>>>>>>> ad410158edf824bd51bc565d10966c4374be934c

    # Method to calculate the addition of two vectors
    def calculate_addition(self):
<<<<<<< HEAD
        v1, v2 = self.update_vectors() 
        if v1 and v2:#Error handling to see if vectors have stored elements 
            add = np.add(v1, v2) #turns lists into NumPy arryas and completes computation
            messagebox.showinfo("Addition Result", f"Sum: {add}") #displays result
            self.display(v1, v2, add) #plots result
            
    # Method to calculate the subtraction of two vectors
    def calculate_subtraction(self):
        v1, v2 = self.update_vectors()
        if v1 and v2:#Error handling to see if vectors have stored elements 
            diff = np.subtract(v1, v2)#turns lists into NumPy arryas and completes computation
            messagebox.showinfo("Subtraction Result", f"Difference: {diff}")#displays result
            self.display(v1, v2, diff)#plots result
            
    # Method to calculate the dot product of two vectors 
    def calculate_dot_product(self):
        v1, v2 = self.update_vectors()
        if v1 and v2:#Error handling to see if vectors have stored elements 
            dot_product = np.dot(v1, v2)#turns lists into NumPy arryas and completes computation
            messagebox.showinfo("Dot Product Result", f"Dot Product: {dot_product}")#displays result

    # Method to calculate the cross product of two vectors
    def calculate_cross_product(self):
        v1, v2 = self.update_vectors()
        if v1 and v2: #Error handling to see if vectors have stored elements  
            cross_product = np.cross(v1, v2)#turns lists into NumPy arryas and completes computation        
            messagebox.showinfo("Cross Product Result", f"Cross Product: {cross_product}")#displays result
            self.display(v1, v2, cross_product)#plots result
            
    # Display welcome message with instructions
=======
        v1, v2 = self.update_vectors()
        if v1 and v2:
            add = np.add(v1, v2)
            messagebox.showinfo("Addition Result", f"Sum: {add}")
            self.display(v1, v2, add)
#adds vectors and displays results 
    def calculate_subtraction(self):
        v1, v2 = self.update_vectors()
        if v1 and v2:
            diff = np.subtract(v1, v2)
            messagebox.showinfo("Subtraction Result", f"Difference: {diff}")
            self.display(v1, v2, diff)
#subtracts vectors and displays results 
    def calculate_dot_product(self):
        v1, v2 = self.update_vectors()
        if v1 and v2:
            dot_product = np.dot(v1, v2)
            messagebox.showinfo("Dot Product Result", f"Dot Product: {dot_product}")

#dots vectors and displays results 
    def calculate_cross_product(self):
        v1, v2 = self.update_vectors()
        if v1 and v2:
            cross_product = np.cross(v1, v2)
            messagebox.showinfo("Cross Product Result", f"Cross Product: {cross_product}")
            self.display(v1, v2, cross_product)
         #takes cross product of vectors and displays results    
>>>>>>> ad410158edf824bd51bc565d10966c4374be934c
    def show_welcome_message(self):
        messagebox.showinfo(f"Welcome/n", "Welcome to Vector Analysis! Your one-stop shop for all things vectors. Please enter two vectors.")



# Initialize object plottor of class Vector
plotter = Vector()



# Labels and Inputs for Vector 1
Label(UI, text="Vector 1", font=("Arial", 12, "bold"), bg="#E8F6F3").grid(row=1, column=0, pady=5)
x_entry1 = Entry(UI, width=10, font=("Arial", 12), borderwidth=2)
x_entry1.grid(row=1, column=1, padx=5, pady=5)
y_entry1 = Entry(UI, width=10, font=("Arial", 12), borderwidth=2)
y_entry1.grid(row=1, column=2, padx=5, pady=5)
z_entry1 = Entry(UI, width=10, font=("Arial", 12), borderwidth=2)
z_entry1.grid(row=1, column=3, padx=5, pady=5)

# Labels and Inputs for Vector 2
Label(UI, text="Vector 2", font=("Arial", 12, "bold"),  bg="#E8F6F3").grid(row=2, column=0, pady=5)
x_entry2 = Entry(UI, width=10, font=("Arial", 12), borderwidth=2)
x_entry2.grid(row=2, column=1, padx=5, pady=5)
y_entry2 = Entry(UI, width=10, font=("Arial", 12), borderwidth=2)
y_entry2.grid(row=2, column=2, padx=5, pady=5)
z_entry2 = Entry(UI, width=10, font=("Arial", 12), borderwidth=2)
z_entry2.grid(row=2, column=3, padx=5, pady=5)


# Button used for title so if clicked it offers information on how to use application
title_button = Button(UI, text="Vector Analysis!", font=("Arial", 18, "bold"), bg="#f0f0f0", command=plotter.show_welcome_message)
title_button.grid(row=0, column=0, columnspan=6, pady=10)

# Buttons Placed on UI corrosponding to different methods in class Vector
plot_button = Button(UI, text="Plot Vectors", font=("Arial", 10, "bold"), bg="#3498db", fg="white", width=15, command=plotter.update_vectors)
plot_button.grid(row=3, column=0, columnspan=4, pady=10)
add_button = Button(UI, text="Addition", font=("Arial", 10, "bold"), bg="#2ecc71", fg="white", width=15, command=plotter.calculate_addition)
add_button.grid(row=4, column=0, padx=5)
sub_button = Button(UI, text="Subtraction", font=("Arial", 10, "bold"), bg="#e74c3c", fg="white", width=15, command=plotter.calculate_subtraction)
sub_button.grid(row=4, column=1, padx=5)
dot_button = Button(UI, text="Dot Product", font=("Arial", 10, "bold"), bg="#f39c12", fg="white", width=15, command=plotter.calculate_dot_product)
dot_button.grid(row=4, column=2, padx=5)
cross_button = Button(UI, text="Cross Product", font=("Arial", 10, "bold"), bg="#9b59b6", fg="white", width=15, command=plotter.calculate_cross_product)
cross_button.grid(row=4, column=3, padx=5)

#generates UI
UI.mainloop()
