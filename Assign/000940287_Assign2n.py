first_name=str(input('Input your name: '))
Celsius=float(input('Input current temperature in Celsius: '))

Fahrenheit = (1.8*Celsius) + 32
print('the current temperature in Celsius is %.2f' % Fahrenheit)

if Celsius>21:
    print(f'{first_name}, it is warm outside.')
elif Celsius<21:
    print(f'{first_name}, it is cool outside.')
else:
    print(f'{first_name}, it is perfect outside.')

