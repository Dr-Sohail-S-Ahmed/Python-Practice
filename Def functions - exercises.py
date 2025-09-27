def area(l,h):
    shape = input("Shape Name: ")
    if shape == "rectangle":
        return l * h
    elif shape == "triangle":
        return 0.5 * l * h
    else:
        return "Incorrect Shape"
print(area(20,4))

# FUNCTION 1
def print_pattern():
    stars = int(input("No. of stars: "))     # 'input' is always a string
    # pattern = ""
    for i in range(1, stars + 1):
        # pattern += "*"
        print("*" * i)
print_pattern()

# FUNCTION 2
def print_pyramid(n=5):                    # uses a default argument
    for i in range(n):
        s = ''
        for j in range(i+1):
            s = s + '*'                    # builds star string manually
        print(s)
print_pyramid()

# Both functions above give the same result with differences being 1st is direct printing while 2nd is manual printing, 1st uses default input...
# ...while 2nd takes user input, 1st is short, quick & easy to read while 2nd is longer & more customizable, 1st has no nested loop while 2nd does