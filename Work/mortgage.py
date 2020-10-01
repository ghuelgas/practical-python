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
month = 0
extra = 1000

while principal > 0:
    month = month + 1
    if month <= 12:
        principal = principal * (1 + rate / 12) - (payment + extra)
    else:
        principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment


print('Total paid', total_paid)
print( 'Month', month)

# Exercise 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    month = month + 1
    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra)
    else:
        principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment


print('Total paid', total_paid)
print( 'Month', month)

# Exercise 1.9

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    month = month + 1
    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra)
    else:
        principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    print(month, total_payed, principal)
    
print('Total paid', total_paid)
print( 'Month', month)
