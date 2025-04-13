bill_amt = float(input("What is the bill amount: "))
tip_perc = float(input("What is the tip percentage: "))/100

tip_amt = tip_perc  * (bill_amt)
total_bill = bill_amt + tip_amt

print(f"The tip amount is ${tip_amt :.2f}")
print(f"The total bill amount is ${total_bill :.2f}")