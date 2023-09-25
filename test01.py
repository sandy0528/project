import datetime
x = datetime.datetime.now()

first_name = "Sandy"
#birth_year_month = [1979,4]

birth_year_month=[]
y=int(input('Input your birth year: '))
birth_year_month.append(y)
m=y=int(input('Input your birth month: '))
birth_year_month.append(y)

today_year_month=[x.year,x.month]

if today_year_month[1]>=birth_year_month[1]:
  age = today_year_month[0] - birth_year_month[0]
else:
  age=today_year_month[0] - birth_year_month[0]-1

print(f'My name is {first_name}. I am {age} years old.')

#  differences1: Lists are used to store multiple items in a single variable; Dictionaries are used to store data values in key:value pairs.
#  differences2: List items are indexed; Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# similarity: both of list and  dictionaries items are ordered, changeable, and allow duplicate values.