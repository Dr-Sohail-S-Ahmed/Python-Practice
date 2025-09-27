weight  = int(input("Weight: ")) # as input function always returns a string, it must be converted to a number
unit = input("kg (K), lb (L): ")
if unit.upper() == "K": # '.upper' function can read both upper & lower cases
    converted = weight / 0.45
    print("Weight in lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in kgs: " + str(converted))