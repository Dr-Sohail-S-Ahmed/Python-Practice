pakistani = ["biryani", "haleem", "zarda", "kheer"]
chinese = ["shawarma", "chowmein", "manchurian", "rice roll"]
italian = ["pasta", "pizza"]

dish = input("Enter a dish name: ")
#   to find an item in a number of lists
if dish in pakistani:
    print("This is a Pakistani cuisine")
elif dish in chinese:
    print("This is Chinese cuisine")
elif dish in italian:
    print("This is an Italian cuisine")
else:
    print("I'm unaware of this cuisine")