"""
1 percent on the first $50,000.
2 percent on the amount over $50,000 up to $75,000.
3 percent on the amount over $75,000 up to $100,000.
4 percent on the amount over $100,000 up to $250,000.
5 percent on the amount over $250,000.

"""
total_tax = 0
tax_rate = 0
income = int(input('Enter the income:\n'))


if 250000 < income:
    tax_rate = 0.05
    income_for_tax = income - 250000
    total_tax = income_for_tax * tax_rate
    income = 250000

if 100000 < income <= 250000:
    tax_rate = 0.04
    income_for_tax = income - 100000
    total_tax = total_tax + income_for_tax * tax_rate
    income = 100000

if 75000 < income <= 100000:
    tax_rate = 0.03
    income_for_tax = income - 75000
    total_tax = total_tax + income_for_tax * tax_rate
    income = 75000

if 50000 < income <= 75000:
    tax_rate = 0.02
    income_for_tax = income - 50000
    total_tax = total_tax + income_for_tax * tax_rate
    income = 50000

if income <= 50000:
    tax_rate = 0.01
    total_tax = total_tax + income * tax_rate

print('The tax payable would be $%0.1f' %total_tax)
# 5000 0.03 150                 20000 * 0.02 400
# 25000 0.02 500                50000* 0.01 500
# 50000 0.01 500

