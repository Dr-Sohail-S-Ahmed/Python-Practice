dict = {"China":143, "India":136, "USA":32, "Pakistan":21}
#      key ↑  |  ↑ value

# PRINTING DICTIONARY IN FOLLOWING FORMAT: (country name) ==> (population)
for key,value in dict.items():
    print(f"{key} ==> {value}")

print(" ")

# ADD/REMOVE COUNTRY NAME
task = input("Add/Remove: ")
cn = input("Country name (case sensitive): ")

if task == "add":
    if cn in dict:
        print("Already listed")
    else:
        pl = input("Population: ")
        dict[cn] = pl
        print("Country Added")
        print("New Dictionary: ", dict)
elif task == "remove":
    if cn in dict:
        del dict[cn]
        print("Country Removed")
        print("Revised Dictionary: ", dict)
    else:
        print("Country Not Listed")