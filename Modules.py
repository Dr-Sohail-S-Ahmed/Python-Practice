# Modules are a compilation of functions/commands created by other users for easier working with Python
# In order to use a module, it must be called upon by using 'import' command e.g. import math
# In order to import submodule, it must be called upon by using 'import' e.g. import urllib.parse
#   [it must be remembered that importing a module doesn't mean that the submodule will also be imported automatically]
# In order to import variable, it must be called upon by using 'from' & 'import' e.g. from math import log, pi
# Additionally, if module is imported with '*', all its variable become accessible without any dotted prefix e.g. from math import *
# CAUTION 1: If 2 modules imported with '*' have a same variable/function name, the latter imported module variable/function is implemented
# CAUTION 2: Importing with '*' sometimes make it difficult to debug the code as it might not be clear which module is supplying the variable/function (due to name collision) & readability of the code is effected

import math
print(math.sqrt(25))        # square root
print(math.pi)              # value of pi
print(math.ceil(2.3))       # ceiling
print(math.floor(2.3))      # floor
# Other functions can also be used. Can read about them online or in Command Prompt > Python
# > import(module_name) > dir(module_name)
# OR in PyCharm > import(module_name) > print(dir(module_name))

import calendar
print(calendar.month(2024,2))   # print calendar for a month
print(calendar.isleap(2024))                    # verify year being leap year

print(" ")

# So long as the custom module is in the same folder as the file calling it 'import' command is sufficient but
# if the module is elsewhere then the following method is used:
import sys
sys.path.append(r"C:\Users\Admin\PycharmProjects\PYTHON PRACTICE\venv")
# sys.path.append(r"C:\Users\Admin\PycharmProjects\PYTHON PRACTICE\venv")
# 'r' in the above syntax denotes raw string telling Python to treat '\' literally otherwise Python treats them
# as the initiation of escape sequence (as in '\n' for new line, '\t' for horizontal tab, etc.)
# Additionally, similar result can also be attained by replacing all '\' with '\\'

import mymodule
print(mymodule.square_area(5))
print(mymodule.triangle_area(2,3))
print(mymodule.rectangle_area(2,4))
print(mymodule.circle_area(10))
