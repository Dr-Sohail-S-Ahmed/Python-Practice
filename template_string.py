name = "Sohail"
age = 25

# After printing the message, f-string loses its structure i.e. placeholders also become part of the string
formatted_string = f"My name is {name} & my age is {age}."
print(formatted_string)

# Even after printing the message, t-strings [Python 3.14] doesn't lose its structure & produce template object
template_string = t"Your name is {name} & you're {age} years old."
print(template_string.strings)          # prints string part of template_string above
print(template_string.interpolations)   # prints placeholder values
print(template_string.values)           # prints values printed in placeholder values
print(template_string)  # (AFTER PYTHON UPDATE, RECHECK WHETHER THIS PRINTS THE STRING OR NOT)