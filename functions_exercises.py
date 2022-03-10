#1
from colorsys import TWO_THIRD


def is_two(x):
    return x == '2' or x == 2
        

is_two(2)


#2.
def is_vowel(x):
    if type(x) == str and len(x) == 1:
        return x.lower() in 'aeiou'

is_vowel('x')
is_vowel('a')
is_vowel('W')

#3.
def is_constonant(x):
    if type(x) == str:
        only_letters = x.isalpha()
        return only_letters and not is_vowel(x)
        # Madelines code above
    x = x.lower()
    if is_vowel(x) == True:
        return False
    else:
        return True

is_constonant('a')

#4.

def capitalize_starting_consonant(x):
    if type(x) != str:
        return False
    first_letter = x[0]
    if is_consonant(first_letter):
        x = x.capitalize
    return x
# madelienes coade above

def capitalize(word):
    word = word.capitalize()
    return word

capitalize('matthew')

# 5.
def calculate_tip(bill, tip_percentage =0.2):
    if type(bill) != float:
        return False
    if tip_percentage < 0 or tip_percentage > 1:
        return 'please enter a tip amount between 0 and 1'
    total = bill * tip_percentage
    return total

calculate_tip(12.23, .15)

# 6.
def apply_discount(price, discount):
    deal = price * discount
    total = price - deal
    return total

apply_discount(123, .34)

# 7.
def handle_commas(word):
        count = 0
        if type(word) != str:  
            return 'input must be a string'  
        for n in word:
            if n == (','):
                count += 1
        return int(count)

handle_commas('1,00,123,123,0')

# 8.
def get_letter_grade(num):
    if type(num) == int or type(num) == float:
        if num > 89:
            return  'A'
        elif num > 79:
            return  'B'
        elif num > 69:
            return  'C'
        elif num > 59:
            return  'D'
        else:
            return  'F'

get_letter_grade(71)

# 9.
def remove_vowels(word):
    if type(word) != str:
        return False
    output = ''
    for v in 'aeiou':
        #if is_consonant(word): output += v return output
        word = word.replace(v,'')
    return word

remove_vowels('banana')

# 10
def normalize_name(name):
    name1 = name.strip()
    name2 = name1.replace(' ', '_')
    return name2.lower()

normalize_name(' Matthew Luna')

# madeleines
def normalize_name(string):
    output = ''
    string = string.lower()
    for character in string:
        if character.isidentifier() or character == ' ':
            output += character
    output = output.strip()
    output = output.replace(' ', '_')
    return output


# 11 MADELEINES code
somenums = [1,2,3,4]
for i, num in enumerate(somenums):
    print('index: ', i)
    print(num)

    def cumulative_sum(somenums):
        output = []
        for i, num in enumerate(somenums):
            sum_so_far = sum(somenums[:i + 1])
            output.append(sum_so_far)
        return output