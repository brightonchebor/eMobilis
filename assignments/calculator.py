print('Please ensure the first number is greater than the second')
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
print('Choose the operation(addition, subtraction, multiplication, or division):')
operation = str(input('>'))

def addition():
    print(f'{num1} + {num2} = {num1 + num2}')

def subtraction():
    print(f'{num1} - {num2} = {num1 - num2}')

def multiplication():
    print(f'{num1} * {num2} = {num1 * num2}')

def division():
    print(f'{num1} / {num2} = {num1 / num2}')   

if operation == 'addition':
    addition()
elif operation == 'subtraction':
    subtraction()
elif operation == 'multiplication':
    multiplication()
else:
    division()                