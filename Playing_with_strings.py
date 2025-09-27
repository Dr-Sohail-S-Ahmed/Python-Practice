# Triple quotes (""" or ''') are used for multi-line strings or docstrings while hash (#) is used for single-line comment
""" '>>>' is prompt used in the Python interactive interpreter (Read, Evaluate, Print, Loop = REPL) for Python command or expression
to be executed in the interactive shell. It's neither string nor comment"""
# 'Ctrl+/' can be used on highlight lines to toggle commenting

course = "Python for Beginners"
print(course.upper())   # returns new string
print(course)   # confirms that original strings hasn't been altered
print(course.find("B")) # "course.find" is case sensitive (& begins with 0 instead of 1) therefore any alphabet that it's unable to find in the string will be displayed as "-1" only
print(course.find("for"))
print(course.replace("for", "4"))   # doesn't alter original string but only displays with replacement
print("thn" in course)  # verifies whether or not particular text/value is present in the original string