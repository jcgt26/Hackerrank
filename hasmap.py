
def mapToDictionary(words: list) -> dict:
    for word in words:
        yield word
    
if __name__=='__main__':
    words  = 'Moin was geht'.split()
    ransome = 'was geht'
    magazine = dict()
    wordsGenerator =  mapToDictionary(words)

    for word in range(0,len(words)):
        word = next(wordsGenerator)
        magazine[word] = word
    
    print(magazine['moin'])
