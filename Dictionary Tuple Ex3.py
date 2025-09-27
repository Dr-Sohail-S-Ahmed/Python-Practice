import math

# DEFINING CIRCLE CALCULATIONS
def circle_calc():              # 'r' not mentioned in function name bcz it's defined within the function
    r = float(input("Enter radius: "))
    calc = input("Name Calculation (area, circumference, diameter): ")
    if calc.lower() == "area":
        a = math.pi * r**2
        print(f"Area = {round(a,2)}")
    elif calc.lower() == "circumference":
        c = 2 * math.pi * r
        print(f"Circumference = {round(c,2)}")
    elif calc.lower() == "diameter":
        d = r * 2
        print(f"Diameter = {round(d,2)}")
    else:
        print("Invalid Calculation")
circle_calc()

# DEFINING CIRCLE CALCULATIONS USING MAIN 1
def cir_calc(rad):              # adding 'rad' when defining the function is important as without it error will occur
    a = math.pi * rad**2
    c = 2 * math.pi * rad
    d = 2 * rad
    return a,c,d

if __name__ == '__main__':
    rad = float(input("Enter radius: "))
    a,c,d = cir_calc(rad)
    print(f"Area = {a}, Circumference = {c}, Diameter = {d}")

# DEFINING CIRCLE CALCULATIONS USING MAIN 2
def c_calc(radius):             # 'radius' not defined inside the function therefore mentioned in function name to take it from outside
    area = math.pi * (radius**2)
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return area,circumference,diameter

if __name__=="__main__":
    r = input("Enter a radius:")
    r = float(r)
    x, y, z = c_calc(r)      # it doesn't matter what variable name is used here (e.g. x,y,z) but it's important that all are mentioned...
                             # ...as each value will be taken from the corresponding value from the function defined above (i.e.
                             # ...area,circumference,diameter) [Python matches by position not variable name]
    print(f"area {x}, circumference {y}, diameter {z}")