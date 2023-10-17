def swap_case(stringInput):
    if(len(stringInput) > 1000):
        raise Exception('String out of bounds')
    result = ''
    for char in invert_character_generator(stringInput):
        result += char
    return  result


def invert_character_generator(string):
    for char in string:
        yield char.lower() if char.isupper() else char.upper()

if __name__ == '__main__':
    stringInput = input()
    result = swap_case(stringInput)
    print(result)
