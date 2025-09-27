# 1.Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
# 2.Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area.

shape = input("Select shape: ")

if shape.lower() == "triangle":
    base = float(input("Base: "))
    height = float(input("Height: "))
    area = 1/2 * (base * height)
    print(f"Area of {shape} is " + str(area))   # 1st method of writing string
elif shape.lower() == "rectangle":
    length = float(input("Length: "))
    breadth = float(input("Breadth: "))
    area = length * breadth
    print(f"Area of {shape} is {area}")       # 2nd method of writing string
elif shape.lower() == "circle":
    radius = float(input("Radius: "))
    import math
    area = math.pi * radius**2
    print(f"Area of {shape} is {area}")
else:
    print("Error: Shape not recognized")
"""a simplified version of this code block could be that shape, vertical & horizontal dimensions are taken as input at the start
followed by calculation of triangle or rectangle area as per the shape using the dimensions taken earlier but this couldn't
be used for shapes like a circle as it only requires on dimension which is neither vertical nor horizontal"""