def to_jaden_case(string):
    words = string.split()
    result = ''

    for word in words:
        result += word.capitalize() + ' '

    print(result[:-1])