import json

"""data = {
    "Name": "Hamdan",
    "Age": 10,
    "Name": "Aariz",
    "Age": 7
}"""
# the problem with writing dictionary in this way is that JSON format doesn't allow duplicate keys, as 'Name' &
# 'Age' are written twice, therefore it overwrites the first key with the second one thus json file contains
# only the last key only. A better way would be to write each key separately

data = {}
data["Hamdan"] = {
    "Name": "Hamdan",
    "Age": 10
}
data["Aariz"] = {
    "Name": "Aariz",
    "Age": 7
}

# METHOD 1
with open("test1.json", "w") as json_file1:     # if the file is in a different folder then it can be written as:
                                                # Example:- open("c://book//test1.json", "w")
    json.dump(data, json_file1)      # 'dump' means write to file as object
                                     # 'dump' requires object (i.e. 'data') & file-like object (i.e. 'json_file1')

print("Print File: Method A")
with open("test1.json") as json_file1:  # to see file contents
    data = json.load(json_file1)
    print(data)
# in this case data from the file is printed only

print("First File: Object Description")
json_file1 = open("test1.json", "r")
print(json_file1)
# in this case description of the file object is displayed with '<>'

print("Print File: Method B-1 (print as string)")
p = json_file1.read()
print(p)

print("Print File: Method B-2 (print as dictionary)")
d = json.loads(p)
print(d)
print(type(d))      # confirm in '<>' that the data loaded in its actual dictionary form

# for further verification, separate entries can be taken out & printed from the dictionary
print(d["Hamdan"])          # for complete data
print(d["Hamdan"]["Age"])   # for specific data

print("Print File: Method C (print in separate lines)")
for person in d:
    print(d[person])

    #   This underlying code block is used to print the data from the json file but the one above is simpler
"""loaded_data = {}
with open("test.json") as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)"""


# METHOD 2
s = json.dumps(data)        # 'dumps' means write to file as string
                            # 'dumps' only require object (i.e. 'data')
with open("test2.json", "w") as json_file2:
    json_file2.write(s)

print("Second File: Printed")
with open("test2.json") as json_file2:  # to see file contents
    data = json.load(json_file2)
    print(data)

# to verify the file size for both 'dump' & 'dumps' files but both appear to have similar size (although in
# this instance the size appears to be the same)
import os
print(os.path.getsize("test1.json"))
print(os.path.getsize("test2.json"))

