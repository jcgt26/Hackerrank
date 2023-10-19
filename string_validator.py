def checkChar(stringVal, meetsCondition):
    for char in stringVal:
        if(meetsCondition(char)):
            return True

    return False

if __name__ == '__main__':
    s = input()
    if(len(s) > 1000):
        raise Exception('String out of bounds')
    
    isAlphaNum = lambda character: character.isalnum()
    isAlpha = lambda character: character.isalpha()
    isDigit  = lambda character: character.isdigit()
    isLower = lambda character: character.islower()
    isUpper = lambda character: character.isupper()
    
    print(checkChar(s,isAlphaNum))
    print(checkChar(s,isAlpha))
    print(checkChar(s,isDigit))
    print(checkChar(s,isLower))
    print(checkChar(s,isUpper))

    


