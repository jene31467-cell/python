"""
List comprehension allows you to create a new list in a single line by combining a loop and condition directly within square brackets. This makes the code shorter and often easier to read.
"""
# numbers = [1, 2, 3, 4, 5]
# result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in  numbers]
# print(result)
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) < 4
long_words = list(filter(is_long_word, words))
print(long_words)