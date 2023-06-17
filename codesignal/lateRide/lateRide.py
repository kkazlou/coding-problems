def solution(n):

    hours = n//60
    minutes = n%60
    
    time_str = str(hours) + str(minutes)
    
    sum = 0
    for i in time_str:
        sum += int(i)
    
    return sum