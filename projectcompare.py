print ("COMPARE NUMBER")
print (f"{10 * '='}")

number1 = input('number1 = ')
number2 = input ('number2 = ')
operator = input ('operator = ')

expression = f"{number1} {operator} {number2}"
result =  eval(expression)

print (f'{number1} {operator} {number2} = {result}')