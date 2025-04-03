#Created by Karan, Ahmed, Oliee | 2025
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
from tkinter import messagebox

UI = Tk() #establishes UI through tkinter library 
UI.title('Vector Analysis!') #application name
UI.geometry("570x700") #changes pizel size of UI
UI.configure(bg="#E8F6F3") #chnages background color to gray  
UI.resizable(False, False) #so when application opens it does not let you resize it 




class Vector:
    def __init__(self):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.vector_plot = self.fig.add_subplot(111, projection='3d')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=UI)
        self.canvas.get_tk_widget().grid(row=5, column=0, columnspan=5, pady=20)    # Move plot below inputs
    

    def display(self, v1, v2):
        self.vector_plot.clear()
        max_value = max(
            abs(v1[0]), abs(v1[1]), abs(v1[2]),
            abs(v2[0]), abs(v2[1]), abs(v2[2])
        ) + 1

        
        self.vector_plot.set_xlim([-max_value, max_value])
        self.vector_plot.set_ylim([-max_value, max_value])
        self.vector_plot.set_zlim([-max_value, max_value])

        # Plot Vector A (Red)
        self.vector_plot.plot([0, v1[0]], [0, v1[1]], [0, v1[2]], color='r', linewidth=3, label="Vector A")
        # Plot Vector B (Blue)
        self.vector_plot.plot([0, v2[0]], [0, v2[1]], [0, v2[2]], color='b', linewidth=3, label="Vector B")

        self.vector_plot.set_xlabel('X Axis')
        self.vector_plot.set_ylabel('Y Axis')
        self.vector_plot.set_zlabel('Z Axis')
        self.vector_plot.legend()
        self.canvas.draw()

    def update_vectors(self):
        try:
            v1 = [float(x_entry1.get()), float(y_entry1.get()), float(z_entry1.get())]
            v2 = [float(x_entry2.get()), float(y_entry2.get()), float(z_entry2.get())]
            self.display(v1, v2)
            return v1, v2
        except ValueError:
            messagebox.showinfo(text="Invalid Input! Enter numeric values.")



        
    def calculate_addition(self):
        v1, v2 = self.update_vectors()
        if v1 and v2:
            add = np.add(v1, v2)
            messagebox.showinfo("Addition Result", f"Sum: {add}")

    def calculate_subtraction(self):
        v1, v2 = self.update_vectors()
        if v1 and v2:
            diff = np.subtract(v1, v2)
            messagebox.showinfo("Subtraction Result", f"Difference: {diff}")


    def calculate_dot_product(self):
        v1, v2 = self.update_vectors()
        if v1 and v2:
            dot_product = np.dot(v1, v2)
            messagebox.showinfo("Dot Product Result", f"Dot Product: {dot_product}")


    def calculate_cross_product(self):
        v1, v2 = self.update_vectors()
        if v1 and v2:
            cross_product = np.cross(v1, v2)
            messagebox.showinfo("Cross Product Result", f"Cross Product: {cross_product}")

def show_welcome_message():
    messagebox.showinfo(f"Welcome/n", "Welcome to Vector Analysis! Your one-stop shop for all things vectors. Please enter two vectors.")



# Initialize Plotter
plotter = Vector()

# Centered Title
title_button = Button(UI, text="Vector Analysis!", font=("Arial", 18, "bold"), bg="#f0f0f0", command=show_welcome_message)
title_button.grid(row=0, column=0, columnspan=6, pady=10)

# Labels and Inputs for Vector A
Label(UI, text="Vector A", font=("Arial", 12, "bold"), bg="#f0f0f0").grid(row=1, column=0, pady=5)
x_entry1 = Entry(UI, width=10, font=("Arial", 12), borderwidth=2)
x_entry1.grid(row=1, column=1, padx=5, pady=5)
y_entry1 = Entry(UI, width=10, font=("Arial", 12), borderwidth=2)
y_entry1.grid(row=1, column=2, padx=5, pady=5)
z_entry1 = Entry(UI, width=10, font=("Arial", 12), borderwidth=2)
z_entry1.grid(row=1, column=3, padx=5, pady=5)

# Labels and Inputs for Vector B
Label(UI, text="Vector B", font=("Arial", 12, "bold"),  bg="#E8F6F3").grid(row=2, column=0, pady=5)
x_entry2 = Entry(UI, width=10, font=("Arial", 12), borderwidth=2)
x_entry2.grid(row=2, column=1, padx=5, pady=5)
y_entry2 = Entry(UI, width=10, font=("Arial", 12), borderwidth=2)
y_entry2.grid(row=2, column=2, padx=5, pady=5)
z_entry2 = Entry(UI, width=10, font=("Arial", 12), borderwidth=2)
z_entry2.grid(row=2, column=3, padx=5, pady=5)

# Button to Plot Vectors
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

UI.mainloop()