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

    #check diagonals
    elif abs(alphaToNum[king[0]] - alphaToNum[queen[0]]) == abs(int(king[1]) - int(queen[1])):
        return True

    #else false
    else:
        return False
    
print(check(king, queen))