# Filters in Python
# allows to filter the elements withi the list, tuple, set

numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def is_even(x):
    return x % 2 == 0


# filter(function, iterable)
even_numbers = filter(is_even, numbers)  # this code means filters (method-
# is_even) will be applied on the numbers using
print(list(even_numbers))  # [2, 4, 6, 8]

# filter vowels from the list

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'i', 'o']
vowels = ['a', 'e', 'i', 'o', 'u']


def filter_vowels(letter):
    return letter in vowels


filtered_words = filter(filter_vowels, letters)
print(list(filtered_words))  # ['a', 'e', 'i', 'o']

# pick item if true keep it, else remove it
# it can give less no of items as compared to actual items in the list


