file = open("example.txt", "r")     # File open modes: r = read-only, w = write only, r+ = reading & writing (existing file),
                                    # w+ = reading & writing (overwrite existing or create new file), a = append
content = file.read()
print(content)

print(" ")
print("***")    # Once the file is opened it doesn't close on its own & multiple tasks can be performed with this open file. However, if a task other than related to the opened file is performed the file close automatically in order to perform the other task
print(" ")

with open("example.txt", "w") as file:      # This will not only add new data to the file but will overwrite all previous data
    file.write("A1B2C3 !@#$")
    file.write("\nD4E5F6 %^&* {[()]}")                  # '\n' denotes appending to the next line for writing

file = open("example.txt")  # Alternate method of opening & reading a file
print(file.read())
file.close()

print(" ")
print("###")
print(" ")

with open("WoE.jpeg", "rb") as binary_file: # For opening & printing binary or image files + picture won't be printed but instead only its binary version
    data = binary_file.read()
    print(data)
file.close()

print(" ")
print("!!!")
print(" ")

file = open("WoE.jpeg", "rb")   # Alternate method of opening & printing binary file
print(file.read())
file.close()

print(" ")

print("  prints only file object description")
file = open("example.txt")
print(file)

print("  prints entire file contents")
print(file.read())          # probably automatically closes file also

print("  prints file contents line-wise")
file = open("example.txt")
for line in file:
    print(line)

print("  for word list")
file = open("example.txt")
for wl in file:
    count = wl.split(" ")       # this splits the words into a list with space (" ") as delimiter
    print(count)

print("  for word count")
file = open("example.txt")
for wc in file:
    count = wc.split(" ")
    print(len(count))

print("  writing word count in separate file along with the original lines")
file = open("example.txt")
new_file = open("example_wc.txt", "w+")
for wcf in file:                # wcf variable is referring to wordcount file
    token = wcf.split(" ")      # 'print(token)' can confirm that the lines have been divided into separate words using
                                # space & thus a list of words is displayed for each line
    new_file.write("Word Count: " + str(len(token)) + " > " + wcf)
    new_file.seek(0)            # takes the pointer to beginning of the file
    print(new_file.read())
file.close()
new_file.close()
# Basically, this code block opened an already written file & a new empty file followed by copying the data of the first
# file into the second one but with word count as well

print("   reprinting")
with open("example_wc.txt") as f:
    print(f.read())
print(f.closed)                 # confirms that the file has been closed or not
# This code block is meant to reprint what's already printed just above it but using 'with' statement thus closing the
# file automatically without specifying the closing action (like 'file.close()')