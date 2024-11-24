def mutate_string(string, position, character):
    word = list(string)
    size = len(word)
    if(position < 0 or position > size):
        raise Exception("Index out of bounds")
    word[position] = character

    return ''.join(word)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)