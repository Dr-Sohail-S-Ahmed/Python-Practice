# "" (double quote) & '' (single quote) can both be used for strings
# Using "" is better if there's use of '' inside the string & vice versa to prevent confusion for Python
# Also single quote can also be mentioned as 'Pluto\'s a planet'
# Use \' to get ' e.g. 'What\'s up?' → What's up?
# Use \" to get " e.g. "That's \"cool\"" → That's "cool"
# Use \\ to get \ e.g. "Look, a mountain: /\\" → Look, a mountain: /\
# Use \n to append to newline e.g. "1\n2 3" → 1
#                                             2 3
# """ (triple quotes) are used for docstrings

claim = "Pluto is a planet!"

# CHANGING CASE
print(claim.upper())
print(claim.lower())

# LOCATING SUBSTRING
print(claim.index("uto"))

# STARTING WITH...
print(claim.startswith("planet"))

# ENDING WITH...
print(claim.endswith("planet"))     # '!' mark not mentioned therefore answer is false

# SPLIT UP
print(claim.split())

# STRING LENGTH
print(len(claim))

# SEPARATING CHARACTERS
print([char + '!' for char in claim])

# JOIN STRING 1: STRINGS ONLY
words = ["Goodbye,", "Cruel", "World..."]
separator = " "     # Space as the separator
result = separator.join(words)
print(result)

# JOIN STRING 2: INTEGER ALSO
position = 1
print("I won the ", str(position), "st prize.")     # interger must be converted to string before printing
print("I won the " + str(position) + "st prize.")

# JOIN STRING 3: FORMATTING (str.format)
planet = "Pluto"
place = 9
message = "{}, you'll always be the {}th planet to me.".format(planet, place)       # '{}' is used as placeholder for value to be inserted
print(message)

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
answering = "{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(planet, pluto_mass, pluto_mass/earth_mass, population)
        # ':' marks beginning of formatting specs, '.2' & '.3' specifies the decimal places while ',' in 4th placeholder defines separator for integer
print(answering)

sentence = """Pluto's a {0}.
No. It's a {1}.
Both '{0}' & '{1}' placeholders were assigned a number.""".format("planet", "dwarf planet")
print(sentence)