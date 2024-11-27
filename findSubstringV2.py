
def count_substring(string, sub_string):
    wordSize = len(string)
    subStringSize = len(sub_string)

    if(wordSize < 0 or wordSize > 200):
        raise Exception("Wrong Size of Word")
    
    if(subStringSize < 0 or subStringSize > wordSize):
        raise Exception("Wrong size of substring")

    currentIdx = 0
    counter = 0
    while(currentIdx < wordSize - 1):
        try:
            idx = string.index(sub_string)
            counter+=1
            currentIdx = idx + len(sub_string) - 1
            string = string[currentIdx:]
        except ValueError:
            break # not found
            

    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)