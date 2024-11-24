import re as regx

def count_substring(string, sub_string):
    wordSize = len(string)
    subStringSize = len(sub_string)

    if(wordSize < 0 or wordSize > 200):
        raise Exception("Wrong Size of Word")
    
    if(subStringSize < 0 or subStringSize > wordSize):
        raise Exception("Wrong size of substring")

    pattern  = sub_string
    matches = regx.findall(pattern=pattern, string=string)

    return len(matches)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)