def solution(inputString):
    
    # rev = ''
    # counter = len(inputString)
    
    # while counter > 0:
    #     rev = rev + inputString[counter - 1]
    #     counter = counter - 1
    
    rev = inputString[::-1]
        
    if inputString == rev:
        return True
    else:
        return False
