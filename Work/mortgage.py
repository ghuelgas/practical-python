# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)


# Exercise 1.8


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

while principal > 0:
   
    if month <= 12:
      principal = principal * (1+rate/12) - payment - 1000 
     
    else:
      principal = principal * (1+rate/12) - payment
      
    month = month + 1
    total_paid = total_paid + payment

print('Total paid', total_paid)
print('Months', month)
