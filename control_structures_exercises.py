# Conditional bases


# 1a.
day_of_week = 'monday'

if day_of_week == 'monday':
    print('yes, that\'s today')
else:
    print('please try again')

# 1b.
weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
weekend = ['saturday', 'sunday']

if weekday:
    print('that is a weekday')
else:
    print ('that is not a weekday')

# 1c.
hours_worked = 22
hourly_rate = 60
paycheck = hours_worked * hourly_rate

if hours_worked <= 40:
    print ('your paycheck totals to {}'.format(paycheck * .5))
else:
    print ('your paycheck will be {}'.format(paycheck))  

# 2. LOOP BASICS
#2a. While
i = 5
while i <= 15:
    print (i)
    i += 1

count = 0
while count < 100:
    count = count + 2
    print (count)

count = 100
while count >= -10:
    count = count - 5
    print (count)

count = 2
while count <= 1000000:
    count = count ** 2
    print(count)

count = 100
while count >= 5:
    print (count)
    count = count - 5

# b. FOR loops
#i.
num = int(input('What number are you trying to learn:  '))

for r in range(1, 11):
    print(num, 'x', r, '=', num*i)

# ii.
for i in range(1, 10):
    print (i * i)

#C i. Break and Continue

num = input('Here is an odd number:  ')

for n in range(50):
    if n % 2 == 0:
        continue
    print('Here is an odd number: {}'.format(n))

