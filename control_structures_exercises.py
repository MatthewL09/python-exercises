# Conditional bases


# 1a.
from re import U
from turtle import pos


day_of_week = input('Please input a day of the week: ')

if day_of_week.lower() == 'monday':
    print('yes, that\'s today')
else:
    print('please try again')

# 1b.
weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
weekend = ['saturday', 'sunday']

day_of_week = input('Please input a day of the week: ')

if day_of_week.lower().startswith('s'):
    print('that is not a weekday')
else:
    print ('that is a weekday')

# 1c.
hours_worked = 22
hourly_rate = 60.50
paycheck = hours_worked * hourly_rate

if hours_worked <= 40:
    paycheck = hours_worked * hourly_rate
else:
    overtime_hours = hours_worked -40
    overtime_pay = overtime_hours * 1.5 * hourly_rate
    base_pay = 40 * hourly_rate
    paycheck = base_pay + overtime_pay
    print (paycheck)  

# 2. LOOP BASICS
#2a. While
i = 5
while i <= 15:
    print (i)
    i += 1
    # other options, i = i +1

i = 0
while i < 101:
    print (i)
    i = i + 2

count = 100
while count >= -10:
    print (count)
    count = count + -5

count = 2
while count < 1000000:
    print(count)
    count = count ** 2

count = 100
while count >= 5:
    print (count)
    count = count + -5

# b. FOR loops
#i.
num = int(input('What number are you trying to learn:  '))

for r in range(1, 11):
    #print(num, 'x', r, '=', num*r)
    print(f'{num} X {r} = {int(num) * n}')

# ii.
for i in range(1, 10):
    print (str(i) * i)

#C i. Break and Continue

num = input('Here is an odd number:  ')

for n in range(50):
    if n % 2 != 0:
        print('Here is an odd number: {}'.format(n))
    elif n == 31:
        break

while True:
    posited_num = input('please enter an odd number between 1 and 50: ')
    if posited_num.isdigit():
        if int(posited_num) % 2 == 1 and int(posited_num) <= 50:
            break

type(posited_num)

posited_num = int(posited_num)

for num in range(1,50,2):
    if num == posited_num:
        print('Yikes! skipping:number: ', num)
    else:
        print('Here is an odd number: ', num)


#D. 
while True:
        posited_num = input('please enter a positive integer: ')
        if posited_num.isdigit():
            if int(posited_num) > 0:
                break
posited_num = int(posited_num)
for num in range(0, posited_num, 1):
    print(num)

while True:
        posited_num = input('please enter a positive integer: ')
        if posited_num.isdigit():
            if int(posited_num) > 0:
                break
posited_num = int(posited_num)
for num in range(posited_num, 0, -1):
    print(num)



# 3 FIZZBUZZ
for n in range(1,101):
    print(n)

for n in range(1,101):
    if n % 3 == 0:
        print('fizz')
    else:
        print(n)
    
for n in range(1,101):
    if n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)


for n in range(1,101):
    if (n % 3 == 0) and (n % 5 == 0):
        print('fizzbuzz')
    elif n % 5 == 0:
        print('buzz')
    elif n % 3 == 0:
        print('fizz')
    else:
        print(n)

    # 4. Display a table of powers

while True:
        posited_num = input('please enter a positive integer: ')
        if posited_num.isdigit():
            if int(posited_num) > 0:
                break
proceed = input('DO you want to continue and print a table of powers? :')
if proceed.lower().startswith('y'):
    posited_num = int(posited_num)
    print()
    print('number | squared | cubed')
    print('-------| ------- | ----- |')
    for i in range(1, posited_num +1):
        i_squared = i **2
        i_cubed = i ** 3
        print(f'{i} | {i_square ')

n = input('please enter a number: ')
n = 3
t = {1: [n, n**2, n**3]}
print('number', 'squared', 'cubed')
for num, o in t.items():
    print(o, number, squared, cubed)

## Python program to print the data
d = {1: ["Python", 33.2, 'UP'],
2: ["Java", 23.54, 'DOWN'],
3: ["Ruby", 17.22, 'UP'],
10: ["Lua", 10.55, 'DOWN'],
5: ["Groovy", 9.22, 'DOWN'],
6: ["C", 1.55, 'UP'] }
print ("Pos,Lang,Percent,Change")
for k, v in d.items():
    lang, perc, change = v
    print (k, lang, perc, change)


# 5.
while true:
    user_num = input('plese enter a number between 0 and 100: ')
    if user_num.isdigit():
        user_num = int(user_num)
        if user_num < 0 or user_num > 100:
            continue
        break


grade = int(user_num)
if grade in range(60):
    grade = 'F'
elif grade in range(60,67):
    grade = 'D'
elif grade in range(67,80):
    grade = 'C'


print(grade)


#6
bookshelf = [ 
    {'title': 'Wheel of Time',
    'author': 'Robert Jordan',
    'genre': 'Science Fiction'},
    {'title': 'Harry Potter',
    'author': 'J.K. Rowling',
    'genre': 'Children\s Book'}, 
    {'title':'The Four Agreements',
    'author': 'Don Miguel Ruiz',
    'genre': 'Self Help'}]

for book in bookshelf:
    print('We are living ina single dictionary here')
# list comprehension with the brackets around print statment
# equal to for key in book: print(key,book[key])
    [print(key, ': ', book[key]) for key in book]
    print('-------')]

picked_genre = input('Please pick a genre an I will return the titles fo that genre on shelf. \n')

matches = []
for book in bookshelf:
    if book['genre'].lower() == picked_genre.lower():
        matches.append(book['title'])

if matches == []:
    print('there are no books in that genre available. Please check later')
else:
    print('I have the following titles in the genre {}'.format(picked_genre))