def split_and_join(line):
    result = '-'.join(line.split(' '))
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
