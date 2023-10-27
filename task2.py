#! python3
"""
###### Task 2
Ask the user to enter in the prices of 5 items in dollars.cents (eg 10.34).  Find the total value of all items and then calculate the total price including 5% GST and 7% PST

Sample:
Enter in price of item #1: 10.25
Enter in price of item #2: 11.45
Enter in price of item #3: 13.85
Enter in price of item #4: 9.25
Enter in price of item #5: 10.25
Your subtotal is 55.05
Your GST is 2.75
Your PST is 3.85
Your total is 61.65
"""
total_value=0

for i in range(5):
    price=float(input("enter the price of item{}:$".format(i+1)))
    total_value+=price

gst_ammount =total_value * 0.05 
pst_ammount =total_value * 0.07 
final_price= total_value + gst_ammount + pst_ammount
print("the total value of all iteme is:${:2F}".format(total_value))
print("the final price including 5% GST and 7% PST is: ${:.2f}".format(final_price))
