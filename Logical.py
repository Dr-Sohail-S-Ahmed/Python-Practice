price = 13
print(price > 10 and price < 30)    # both conditions must be met
print(price > 15 or price == 20)    # at least one condition must be met
print(not price >= 10)  # if the condition is me then opposite boolean answer is given
# In this case variable 'price'"' is only defined once & the same value is used again whereas if some calculation is carried out & the new value also has the variable label 'price', Python will consider this new value in the next calculation instead of the first original value