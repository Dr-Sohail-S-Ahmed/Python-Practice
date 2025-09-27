# this was created as practice
length = float(input("Length: "))   # float make the code more robust as it can tackle both whole & decimal numbers
unit = input("in (I) or cm (C): ")
if unit.upper() == "I":
    converted = length * 2.54
    print("Length in centimeters: " + str(converted))
else:
    converted = length * 0.3937
    print("Length in inches: " + str(converted))