a= float(input("Enter the cost of item  = "))
b= float(input("Enter the cost of item  = "))
c= float(input("Enter the cost of item  = "))
meal= a+b+c
tax_rate= 0.10
tip_rate= float(input("Enter the tip in % = "))
tip= tip_rate/100
tip_amt= meal*tip
tax= meal*tax_rate
total= meal+tax+tip_amt
print("The total bill is:(RS) = ",total)