# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

LIST_OF_ITEMS = list()

def parseCommand(line, minimalNumberOfParameters = 1):
    if(len(line.split()) < minimalNumberOfParameters):
        raise ValueError('Missing params or command')
    [command, *params] = line.split()

    return command, params


def insertToListOfItems(rawIndex, rawItem):
    index = int(rawIndex)
    item = int(rawItem)
    LIST_OF_ITEMS.insert(index,item)

def printListOfItems():
    print(LIST_OF_ITEMS)

def removeItemFromList(rawItem):
    item = int(rawItem[0])
    if(item in LIST_OF_ITEMS):
        LIST_OF_ITEMS.remove(item)

def appendItemInList(rawItem):
    item = int(rawItem[0])
    LIST_OF_ITEMS.append(item)

def sortListOfItems():
    LIST_OF_ITEMS.sort()

def reverseListOfItems():
    LIST_OF_ITEMS.reverse()

def popItemFromList():
    LIST_OF_ITEMS.pop()


def executeCommand(command, values):

    if(validated(command, values) == False):
        raise ValueError('Wrong use of command')
    if(command == 'insert') :
        insertToListOfItems(values[0], values[1])
    if(command == 'print'):
        printListOfItems(),
    if(command == 'remove'):
        removeItemFromList(values),
    if(command == 'append'):
        appendItemInList(values),
    if(command == 'sort'):
        sortListOfItems(),
    if(command == 'reverse'):
        reverseListOfItems()
    if(command == 'pop'):
        popItemFromList()


def validated(command, value):
    if(command == 'insert'):
        return len(value) == 2

    if(command == 'remove'):
        return len(value) == 1

    if(command == 'append'):
        return len(value) == 1



if __name__ == '__main__':
    commandHistory = list()
    numberOfCommands = int(input())

    for i in range(0, numberOfCommands):
        [command, params] = parseCommand(input())
        executable = executeCommand(command, params)
