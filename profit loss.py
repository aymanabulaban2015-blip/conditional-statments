Actual_cost=float(input('Please enter the actual product price : '))
Sale_amount=float(input('Please enter the sale amount : '))

if Sale_amount>Actual_cost:
    Profit_amount=Sale_amount-Actual_cost
    print(f'profit value =  {Profit_amount}')
else:
    print('No profit !')