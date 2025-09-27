# CONTINUE: 1.see class explanation from gemini & add to creating class.py & pratice + 2.continue to data science roadmap

def calculate_area(shape, *dimensions):
    """
    Calculates the area of a shape based on its type and dimensions.

    Args:
        shape (str): The shape ("triangle", "rectangle", or "circle").
        *dimensions: Variable-length tuple containing the required dimensions for the shape.

    Returns:
        float: The calculated area, or None if an error occurs.

    Raises:
        ValueError: If the shape is invalid or the dimensions are non-positive.
    """

    if shape.lower() == "triangle":
        if len(dimensions) != 2:
            raise ValueError("Triangle requires base and height.")
        base, height = dimensions
        area = 0.5 * base * height
    elif shape.lower() == "rectangle":
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires length and breadth.")
        length, breadth = dimensions
        area = length * breadth
    elif shape.lower() == "circle":
        if len(dimensions) != 1:
            raise ValueError("Circle requires radius.")
        radius = dimensions[0]
        area = math.pi * radius**2
    else:
        raise ValueError("Invalid shape. Please enter 'triangle', 'rectangle', or 'circle'.")

    if any(dim <= 0 for dim in dimensions):
        raise ValueError("Dimensions must be positive numbers.")

    return area

# Example usage
shapes = ["triangle", "rectangle", "circle", "invalid"]
dimensions = [(5, 3), (4, 2), (2,), ("invalid",)]

for i in range(len(shapes)):
    shape = shapes[i]
    try:
        area = calculate_area(shape, *dimensions[i])
        if area is not None:  # Only print if area is calculated successfully
            print(f"Area of {shape}: {area}")
    except ValueError as e:
        print(e)