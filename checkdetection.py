#Test case: 
king = "B7"
queen = "D5"

alphaToNum = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
}

def check(king, queen):

    #check if column or row is same
    if (king[0] == queen[0]) or (king[1] == queen[1]):
        return True

    # check diagonals
    # diagonal movement will always have the lateral and vertical equal to each other, remove negatives with abs 
    elif abs(alphaToNum[king[0]] - alphaToNum[queen[0]]) == abs(int(king[1]) - int(queen[1])):
        return True
    # ran into issue with abs(king[1] - queen[1]) since it was a string and had typeerror, had to declare as int


    #else false
    else:
        return False
    
print(check(king, queen))