# test case 
# phrase = "<[{(yay)}]>"

def has_balanced_brackets(phrase):

    # dictionary for pair
    bracketPair = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }

    # init both open and closed list to store
    openBracket = []
    closedBracket = []

    # iterate through input to split open and closed brackets
    for char in phrase:
        if char in bracketPair.keys():
            openBracket.append(char)
        elif char in bracketPair.values():
            closedBracket.append(char)
        
    # auto pass if not even amount of brackets
    if len(openBracket) != len(closedBracket):
        return False
    
    # check to see if first open bracket is equal to last closed bracket and step through
    for i in range(len(openBracket)):
        if bracketPair[openBracket[i]] != closedBracket[-i-1]:
            return False
    
    return True

phrase = input("Phrase to check for balanced brackets: ")
print(has_balanced_brackets(phrase))





