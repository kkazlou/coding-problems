def solution(score1, score2):
    
    if score1 == 6 and 0 <= score2 <= 4:
        return True
    if score2 == 6 and 0 <= score1 <= 4:
        return True
    if score1 == 7 and 5 <= score2 <= 6:
        return True
    if score2 == 7 and 5 <= score1 <= 6:
        return True
        
    return False