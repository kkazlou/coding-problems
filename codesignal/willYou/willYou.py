def solution(young, beautiful, loved):
    
    if (young and beautiful) and not loved:
        return True
    elif loved and not (young and beautiful):
        return True
    else:
        return False