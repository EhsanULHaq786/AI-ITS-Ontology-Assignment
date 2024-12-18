#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from owlready2 import *
import math

# Create a new ontology
onto = get_ontology("http://example.org/shape_ontology.owl")

# Define the ontology structure
with onto:
    # Base Class: Shape
    class Shape(Thing):
        pass

    # Data Properties
    class has_base(DataProperty, FunctionalProperty):
        range = [float]

    class has_height(DataProperty, FunctionalProperty):
        range = [float]

    class has_side(DataProperty, FunctionalProperty):
        range = [float]

    class has_radius(DataProperty, FunctionalProperty):
        range = [float]

    class has_area(DataProperty, FunctionalProperty):
        range = [float]

    class has_volume(DataProperty, FunctionalProperty):
        range = [float]

    # 2D Shape Class
    class TwoDShape(Shape):
        pass

    # Triangle Class
    class Triangle(TwoDShape):
        pass

    # Square Class
    class Square(TwoDShape):
        pass

    # 3D Shape Class
    class ThreeDShape(Shape):
        pass

    # Cube Class
    class Cube(ThreeDShape):
        pass

    # Sphere Class
    class Sphere(ThreeDShape):
        pass

    # Create instances for testing
    triangle1 = Triangle("Triangle1")
    triangle1.has_base = 5.0
    triangle1.has_height = 10.0
    triangle1.has_area = 0.5 * triangle1.has_base * triangle1.has_height

    square1 = Square("Square1")
    square1.has_side = 4.0
    square1.has_area = square1.has_side ** 2

    cube1 = Cube("Cube1")
    cube1.has_side = 3.0
    cube1.has_volume = cube1.has_side ** 3

    sphere1 = Sphere("Sphere1")
    sphere1.has_radius = 3.0
    sphere1.has_volume = (4 / 3) * math.pi * (sphere1.has_radius ** 3)

# Save the ontology to a file
onto.save(file="shapes_ontology.owl", format="rdfxml")
print("Ontology saved as 'shapes_ontology.owl'")


# In[ ]:


from owlready2 import *
import tkinter as tk
from tkinter import ttk, messagebox
import math

# Functions to perform calculations
def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_square_area(side):
    return side ** 2

def calculate_cube_volume(side):
    return side ** 3

def calculate_sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)

# User Interface with Enhanced Styling
def open_ui():
    def triangle_area():
        try:
            base = float(entry_base.get())
            height = float(entry_height.get())
            area = calculate_triangle_area(base, height)
            messagebox.showinfo("Triangle Area", f"Area of Triangle: {area:.2f} square units")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for base and height!")

    def square_area():
        try:
            side = float(entry_side_square.get())
            area = calculate_square_area(side)
            messagebox.showinfo("Square Area", f"Area of Square: {area:.2f} square units")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for side length!")

    def cube_volume():
        try:
            side = float(entry_side_cube.get())
            volume = calculate_cube_volume(side)
            messagebox.showinfo("Cube Volume", f"Volume of Cube: {volume:.2f} cubic units")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for side length!")

    def sphere_volume():
        try:
            radius = float(entry_radius.get())
            volume = calculate_sphere_volume(radius)
            messagebox.showinfo("Sphere Volume", f"Volume of Sphere: {volume:.2f} cubic units")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for radius!")

    # Tkinter Window
    root = tk.Tk()
    root.title("Intelligent Tutoring System - Shapes")
    root.geometry("500x600")
    root.configure(bg="#f0f0f0")

    # Heading
    heading = tk.Label(root, text="Intelligent Tutoring System", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
    heading.pack(pady=10)

    subheading = tk.Label(root, text="Calculate Areas and Volumes of Shapes", font=("Arial", 12), bg="#f0f0f0", fg="#555")
    subheading.pack(pady=5)

    # Section Styling
    def create_section(title, parent):
        frame = tk.Frame(parent, bd=2, relief="groove", bg="#ffffff", padx=10, pady=10)
        tk.Label(frame, text=title, font=("Arial", 12, "bold"), bg="#ffffff", fg="#000").pack(anchor="w", pady=5)
        return frame

    # Triangle Section
    triangle_frame = create_section("Triangle", root)
    triangle_frame.pack(pady=10, fill="x", padx=20)

    tk.Label(triangle_frame, text="Base:", bg="#ffffff").pack(anchor="w")
    entry_base = ttk.Entry(triangle_frame, width=20)
    entry_base.pack(pady=2)

    tk.Label(triangle_frame, text="Height:", bg="#ffffff").pack(anchor="w")
    entry_height = ttk.Entry(triangle_frame, width=20)
    entry_height.pack(pady=2)

    ttk.Button(triangle_frame, text="Calculate Triangle Area", command=triangle_area, style="Custom.TButton").pack(pady=5)

    # Square Section
    square_frame = create_section("Square", root)
    square_frame.pack(pady=10, fill="x", padx=20)

    tk.Label(square_frame, text="Side Length:", bg="#ffffff").pack(anchor="w")
    entry_side_square = ttk.Entry(square_frame, width=20)
    entry_side_square.pack(pady=2)

    ttk.Button(square_frame, text="Calculate Square Area", command=square_area, style="Custom.TButton").pack(pady=5)

    # Cube Section
    cube_frame = create_section("Cube", root)
    cube_frame.pack(pady=10, fill="x", padx=20)

    tk.Label(cube_frame, text="Side Length:", bg="#ffffff").pack(anchor="w")
    entry_side_cube = ttk.Entry(cube_frame, width=20)
    entry_side_cube.pack(pady=2)

    ttk.Button(cube_frame, text="Calculate Cube Volume", command=cube_volume, style="Custom.TButton").pack(pady=5)

    # Sphere Section
    sphere_frame = create_section("Sphere", root)
    sphere_frame.pack(pady=10, fill="x", padx=20)

    tk.Label(sphere_frame, text="Radius:", bg="#ffffff").pack(anchor="w")
    entry_radius = ttk.Entry(sphere_frame, width=20)
    entry_radius.pack(pady=2)

    ttk.Button(sphere_frame, text="Calculate Sphere Volume", command=sphere_volume, style="Custom.TButton").pack(pady=5)

    # Styling Buttons
    style = ttk.Style()
    style.configure("Custom.TButton", font=("Arial", 10), borderwidth=5, relief="raised", padding=5, background="#4CAF50", foreground="white")
    style.map("Custom.TButton", background=[("active", "#45a049")])

    root.mainloop()

# Launch the UI
open_ui()


# In[ ]:


from tkinter import ttk, messagebox
import tkinter as tk
import math



# 2D Shapes
def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_square_area(side):
    return side ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rhombus_area(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

# 3D Shapes
def calculate_cube_volume(side):
    return side ** 3

def calculate_sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)

def calculate_cylinder_volume(radius, height):
    return math.pi * (radius ** 2) * height

def calculate_cone_volume(radius, height):
    return (1 / 3) * math.pi * (radius ** 2) * height

# User Interface with Tkinter
def open_ui():
    # Shared function to display results in a message box
    def display_result(shape, value, unit):
        messagebox.showinfo(f"{shape}", f"The result is: {value:.2f} {unit}")

  
    def create_section(title, parent):
        frame = tk.Frame(parent, bd=2, relief="groove", bg="#ffffff", padx=10, pady=10)
        tk.Label(frame, text=title, font=("Arial", 12, "bold"), bg="#ffffff", fg="#000").pack(anchor="w", pady=5)
        return frame

    # Root window
    root = tk.Tk()
    root.title("Intelligent Tutoring System - 2D and 3D Shapes")
    root.geometry("600x800")
    root.configure(bg="#f0f0f0")

    heading = tk.Label(root, text="Intelligent Tutoring System", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
    heading.pack(pady=10)

    subheading = tk.Label(root, text="Calculate Areas of 2D Shapes and Volumes of 3D Shapes", font=("Arial", 12), bg="#f0f0f0", fg="#555")
    subheading.pack(pady=5)

    # 2D Shapes Section
    two_d_frame = create_section("2D Shapes", root)
    two_d_frame.pack(pady=10, fill="x", padx=20)

    # Triangle
    tk.Label(two_d_frame, text="Triangle - Base & Height").pack(anchor="w")
    entry_base = ttk.Entry(two_d_frame, width=10)
    entry_base.pack(side="left", padx=5)
    entry_height = ttk.Entry(two_d_frame, width=10)
    entry_height.pack(side="left", padx=5)
    ttk.Button(two_d_frame, text="Calculate Triangle Area", command=lambda: display_result("Triangle Area", calculate_triangle_area(float(entry_base.get()), float(entry_height.get())), "sq units")).pack(pady=5)

    # Square
    tk.Label(two_d_frame, text="Square - Side Length").pack(anchor="w")
    entry_side_square = ttk.Entry(two_d_frame, width=10)
    entry_side_square.pack()
    ttk.Button(two_d_frame, text="Calculate Square Area", command=lambda: display_result("Square Area", calculate_square_area(float(entry_side_square.get())), "sq units")).pack(pady=5)

    # Circle
    tk.Label(two_d_frame, text="Circle - Radius").pack(anchor="w")
    entry_radius_circle = ttk.Entry(two_d_frame, width=10)
    entry_radius_circle.pack()
    ttk.Button(two_d_frame, text="Calculate Circle Area", command=lambda: display_result("Circle Area", calculate_circle_area(float(entry_radius_circle.get())), "sq units")).pack(pady=5)

    # Rectangle
    tk.Label(two_d_frame, text="Rectangle - Length & Width").pack(anchor="w")
    entry_length_rect = ttk.Entry(two_d_frame, width=10)
    entry_length_rect.pack(side="left", padx=5)
    entry_width_rect = ttk.Entry(two_d_frame, width=10)
    entry_width_rect.pack(side="left", padx=5)
    ttk.Button(two_d_frame, text="Calculate Rectangle Area", command=lambda: display_result("Rectangle Area", calculate_rectangle_area(float(entry_length_rect.get()), float(entry_width_rect.get())), "sq units")).pack(pady=5)

    # 3D Shapes Section
    three_d_frame = create_section("3D Shapes", root)
    three_d_frame.pack(pady=10, fill="x", padx=20)

    # Cube
    tk.Label(three_d_frame, text="Cube - Side Length").pack(anchor="w")
    entry_side_cube = ttk.Entry(three_d_frame, width=10)
    entry_side_cube.pack()
    ttk.Button(three_d_frame, text="Calculate Cube Volume", command=lambda: display_result("Cube Volume", calculate_cube_volume(float(entry_side_cube.get())), "cubic units")).pack(pady=5)

    # Sphere
    tk.Label(three_d_frame, text="Sphere - Radius").pack(anchor="w")
    entry_radius_sphere = ttk.Entry(three_d_frame, width=10)
    entry_radius_sphere.pack()
    ttk.Button(three_d_frame, text="Calculate Sphere Volume", command=lambda: display_result("Sphere Volume", calculate_sphere_volume(float(entry_radius_sphere.get())), "cubic units")).pack(pady=5)

    # Cylinder
    tk.Label(three_d_frame, text="Cylinder - Radius & Height").pack(anchor="w")
    entry_radius_cylinder = ttk.Entry(three_d_frame, width=10)
    entry_radius_cylinder.pack(side="left", padx=5)
    entry_height_cylinder = ttk.Entry(three_d_frame, width=10)
    entry_height_cylinder.pack(side="left", padx=5)
    ttk.Button(three_d_frame, text="Calculate Cylinder Volume", command=lambda: display_result("Cylinder Volume", calculate_cylinder_volume(float(entry_radius_cylinder.get()), float(entry_height_cylinder.get())), "cubic units")).pack(pady=5)

    # Cone
    tk.Label(three_d_frame, text="Cone - Radius & Height").pack(anchor="w")
    entry_radius_cone = ttk.Entry(three_d_frame, width=10)
    entry_radius_cone.pack(side="left", padx=5)
    entry_height_cone = ttk.Entry(three_d_frame, width=10)
    entry_height_cone.pack(side="left", padx=5)
    ttk.Button(three_d_frame, text="Calculate Cone Volume", command=lambda: display_result("Cone Volume", calculate_cone_volume(float(entry_radius_cone.get()), float(entry_height_cone.get())), "cubic units")).pack(pady=5)

    root.mainloop()
open_ui()


# In[ ]:


from tkinter import ttk, messagebox
import tkinter as tk
import math

# Calculation functions for all shapes
def calculate_triangle_area(base, height):
    return 0.5 * base * height
def calculate_square_area(side):
    return side ** 2
def calculate_rectangle_area(length, width):
    return length * width
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)
def calculate_cube_volume(side):
    return side ** 3
def calculate_sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)
def calculate_cylinder_volume(radius, height):
    return math.pi * (radius ** 2) * height
def calculate_cone_volume(radius, height):
    return (1 / 3) * math.pi * (radius ** 2) * height
# Function to display results
def display_result(shape, value, unit):
    messagebox.showinfo(f"{shape}", f"The result is: {value:.2f} {unit}")

# Main User Interface
def open_ui():
    root = tk.Tk()
    root.title("Intelligent Tutoring System - 2D and 3D Shapes")
    root.geometry("600x700")
    root.configure(bg="#f8f9fa")
    # Heading
    tk.Label(root, text="Intelligent Tutoring System", font=("Arial", 18, "bold"), bg="#f8f9fa", fg="#333").pack(pady=10)
    tk.Label(root, text="Calculate Areas of 2D Shapes and Volumes of 3D Shapes", font=("Arial", 12), bg="#f8f9fa", fg="#555").pack(pady=5)
    # Section: 2D Shapes
    two_d_frame = tk.LabelFrame(root, text="2D Shapes", font=("Arial", 12, "bold"), bg="#ffffff", padx=10, pady=10)
    two_d_frame.pack(fill="x", padx=20, pady=10)
    # Triangle
    tk.Label(two_d_frame, text="Triangle (Base & Height):", bg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
    entry_base = ttk.Entry(two_d_frame, width=10)
    entry_base.grid(row=0, column=1, padx=5)
    entry_height = ttk.Entry(two_d_frame, width=10)
    entry_height.grid(row=0, column=2, padx=5)
    ttk.Button(two_d_frame, text="Calculate Triangle Area", command=lambda: display_result("Triangle Area", calculate_triangle_area(float(entry_base.get()), float(entry_height.get())), "sq units")).grid(row=0, column=3, padx=5)
    # Square
    tk.Label(two_d_frame, text="Square (Side):", bg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
    entry_square_side = ttk.Entry(two_d_frame, width=10)
    entry_square_side.grid(row=1, column=1, padx=5)
    ttk.Button(two_d_frame, text="Calculate Square Area", command=lambda: display_result("Square Area", calculate_square_area(float(entry_square_side.get())), "sq units")).grid(row=1, column=3, padx=5)

    # Rectangle
    tk.Label(two_d_frame, text="Rectangle (Length & Width):", bg="#ffffff").grid(row=2, column=0, sticky="w", pady=5)
    entry_length = ttk.Entry(two_d_frame, width=10)
    entry_length.grid(row=2, column=1, padx=5)
    entry_width = ttk.Entry(two_d_frame, width=10)
    entry_width.grid(row=2, column=2, padx=5)
    ttk.Button(two_d_frame, text="Calculate Rectangle Area", command=lambda: display_result("Rectangle Area", calculate_rectangle_area(float(entry_length.get()), float(entry_width.get())), "sq units")).grid(row=2, column=3, padx=5)

    # Circle
    tk.Label(two_d_frame, text="Circle (Radius):", bg="#ffffff").grid(row=3, column=0, sticky="w", pady=5)
    entry_radius_circle = ttk.Entry(two_d_frame, width=10)
    entry_radius_circle.grid(row=3, column=1, padx=5)
    ttk.Button(two_d_frame, text="Calculate Circle Area", command=lambda: display_result("Circle Area", calculate_circle_area(float(entry_radius_circle.get())), "sq units")).grid(row=3, column=3, padx=5)

    # Section: 3D Shapes
    three_d_frame = tk.LabelFrame(root, text="3D Shapes", font=("Arial", 12, "bold"), bg="#ffffff", padx=10, pady=10)
    three_d_frame.pack(fill="x", padx=20, pady=10)

    # Cube
    tk.Label(three_d_frame, text="Cube (Side):", bg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
    entry_cube_side = ttk.Entry(three_d_frame, width=10)
    entry_cube_side.grid(row=0, column=1, padx=5)
    ttk.Button(three_d_frame, text="Calculate Cube Volume", command=lambda: display_result("Cube Volume", calculate_cube_volume(float(entry_cube_side.get())), "cubic units")).grid(row=0, column=3, padx=5)

    # Sphere
    tk.Label(three_d_frame, text="Sphere (Radius):", bg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
    entry_radius_sphere = ttk.Entry(three_d_frame, width=10)
    entry_radius_sphere.grid(row=1, column=1, padx=5)
    ttk.Button(three_d_frame, text="Calculate Sphere Volume", command=lambda: display_result("Sphere Volume", calculate_sphere_volume(float(entry_radius_sphere.get())), "cubic units")).grid(row=1, column=3, padx=5)

    # Cylinder
    tk.Label(three_d_frame, text="Cylinder (Radius & Height):", bg="#ffffff").grid(row=2, column=0, sticky="w", pady=5)
    entry_radius_cyl = ttk.Entry(three_d_frame, width=10)
    entry_radius_cyl.grid(row=2, column=1, padx=5)
    entry_height_cyl = ttk.Entry(three_d_frame, width=10)
    entry_height_cyl.grid(row=2, column=2, padx=5)
    ttk.Button(three_d_frame, text="Calculate Cylinder Volume", command=lambda: display_result("Cylinder Volume", calculate_cylinder_volume(float(entry_radius_cyl.get()), float(entry_height_cyl.get())), "cubic units")).grid(row=2, column=3, padx=5)

    # Cone
    tk.Label(three_d_frame, text="Cone (Radius & Height):", bg="#ffffff").grid(row=3, column=0, sticky="w", pady=5)
    entry_radius_cone = ttk.Entry(three_d_frame, width=10)
    entry_radius_cone.grid(row=3, column=1, padx=5)
    entry_height_cone = ttk.Entry(three_d_frame, width=10)
    entry_height_cone.grid(row=3, column=2, padx=5)
    ttk.Button(three_d_frame, text="Calculate Cone Volume", command=lambda: display_result("Cone Volume", calculate_cone_volume(float(entry_radius_cone.get()), float(entry_height_cone.get())), "cubic units")).grid(row=3, column=3, padx=5)

    root.mainloop()

# Launch the UI
open_ui()

