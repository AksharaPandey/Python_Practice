#format specifiers= {value: flags} format a value based on what flags are inserted

# .(number)f= round to (number) decimal places

price1=3.4567
price2=1234.5678
price3=1234567.8910

print(f"Price 1 is ${price1 :10}")
print(f"Price 2 is ${price2 :,.2f}") #comma as thousand separator
print(f"Price 3 is ${price3 :,.2f}")