fruits= ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


#Exercise 1
uppercased_fruits = [fruit.upper() for fruit in fruits]
uppercased_fruits


#Exercise 2
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
capitalized_fruits


#Exercise 3

fruits_with_more_than_two_vowels = [word for word in fruits if len([letter for letter in word if letter in 'aeiou']) > 2]

def count_vowels(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) > 3]
fruits_with_more_than_two_vowels


#Exercise 4
fruits_with_only_two_vowels = [vowel for vowel in fruits if count_vowels(vowel) == 2]
fruits_with_only_two_vowels

#Exercise 5
more_than_five = [word for word in fruits if len(word) > 5]
more_than_five 

# Exercise 6
exactly_five = [letter for letter in fruits if len(letter) == 5]
exactly_five

#Exercise 7
less_than_five = [letter for letter in fruits if len(letter) < 5]
less_than_five

#Exercie 8
word_length = [len(letter) for letter in fruits]
word_length

#Exercise 9
fruits_with_letter_a = [letter[:-1] for letter in fruits == 'a']
fruits_with_letter_a