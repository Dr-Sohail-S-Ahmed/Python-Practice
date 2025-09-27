# FOR PRINTING PROFITS BASED ON THE MONTHS
profit = [2000, 3000, 4000, 5000, 6000]
total = 0           # (not necessary to mention this in this code block)
                    # for variable 'a = 0', IF CONSIDERING LIST CONTEXT, it refers to the position/location found is a list but...
                    # ...IF JUST ASSIGNING VALUE, it refers to storing value '0' in variable 'a'

for p in range(len(profit)):                            # 'p' is variable, 'range' function assume starting number to be '0' if only single number in mentioned like 'range(5)'
    print("Month ", p+1, ", ", "Profit ", profit[p])    # To print profits month-wise
total = sum(profit)                                     # To sum up numbers
print("Total Profit is", total)


# FOR PRINTING CORRESPONDING PROFIT OF THE MONTH
profit = [2000, 3000, 4000, 5000, 6000]
month_list = ["Jan", "Feb", "Mar", "Apr", "May"]
p = input("Enter profit amount: ")
p = int(p)

found = -1          # here '-1' refers to "no match found yet" or "default value" NOT location
for i in range(len(profit)):    # 'for i in range(len(profit)):' creates sequence of indexes (where 'i' will be 0,1,2,etc.) while...
                                # ...'for i in profit:' directly takes values from the list not indexes
    if p == profit[i]:          # 'if p == profit:' → (this is incorrect bcz 'p' is compared to an entire list rather than 'i'...
                                # ...which is a single item in the list)
        found = i
        break
if found != -1:
    # print(f"You earned {p} in {month[month]}")    →   (this is incorrect bcz 'found' is already used for position/index but here it's being reused as a list which gives error)
    print(f"You earned {p} in {month_list[found]}")
else:
    print(f"You didn't earn {p} in any month")

# When & what would "a = -1" refer to:
    # "a = -1" will be considered ASSIGNING VALUE if no list context is involved
    # "a = -1" will be considered as 'NOT FOUND' in the list when "a != -1" condition is also found in the code (referring to 'if found')
    # "a = -1" will not be considered LAST ELEMENT in the list unless written as "a[-1]"


# 5KM RACE > ASK AT EACH KM ABOUT TIREDNESS > YES: NOT FINISHED, NO: CONGRATS
for km in range(5):
    print(f"You ran {km+1} km(s)")
    tired = input("Are you tired: ")
    if tired == "yes":
        break
if km == 4:     # '4' bcz index starts at 0
    print(f"Congrats! You've completed {km+1}km(s) race.")
else:
    print(f"You didn't finish 5km race.")


# PRINTING PYRAMID OF ASTERISKS
for i in range(1,6):
    a = ""
    for j in range(i):
        a += "*"
    print(a)