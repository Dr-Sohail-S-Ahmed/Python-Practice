# Going through the list until the item required is found
key_location = input("Define location: ")           # this can also be written as 'key_location = "bedroom"' but
                                                    # in this case the key location can't be changed except
                                                    # from within the code
locations = ["garage", "clinic", "toilet", "drawing room", "bedroom", "kitchen", "store room", "closet"]
for x in locations:
    if x == key_location:
        print("Keys found in", x)
        break                           # this command breaks the loop once the target is achieved thus reducing
                                        # the burden on the CPU
    else:
        print("Keys not found in", x)