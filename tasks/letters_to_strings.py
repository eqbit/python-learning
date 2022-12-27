import string

print(string.ascii_lowercase)

def letters_to_numbers(input):
    letters = string.ascii_lowercase
    result = ''

    for letter in input:
        try:
            index = letters.index(letter)
            result += str(index + 1)
        except ValueError:
            continue

    return result
