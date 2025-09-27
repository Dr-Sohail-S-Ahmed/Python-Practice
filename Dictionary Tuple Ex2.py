import statistics as stat

stocks = {"info": [600,630,620],
          "ril": [1430,1490,1567],
          "mtl": [234,180,160]}

# PRINTING DETAILS WITH AVERAGES
def print_all():
    for k,v in stocks.items():
        avg = stat.mean(v)
        print(f"{k} ==> {v} ==> Average {round(avg,2)}")
# print_all()       # This is disabled bcz of the main menu created below as the runs this before the 'main_menu'

# ADDING/APPENDING DATA
def add_stock():
    stk = input("Name of stock: ")
    vlu = float(input("Value of stock: "))
    if stk.lower() in stocks:
        stocks[stk].append(vlu)
    elif stk.lower() not in stocks:
        stocks[stk] = [vlu]
    else:
        print("Invalid Entry")
    print(stocks)
# add_stock()       # This is disabled bcz of the main menu created below as it runs 'add_stock()' before the 'main_menu'

# DEFINING MAIN MENU FOR ALL THE TASKS
def main_menu():
    task = input("Enter Task (print, add): ")
    if task.lower() == "print":
        print_all()
    elif task.lower() == "add":
        add_stock()
    else:
        print("Unsupported Task")
if __name__ == '__main__':
    main_menu()