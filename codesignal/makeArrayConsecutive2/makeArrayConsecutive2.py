def solution(statues):
    
    missing = []
    
    statues.sort()

    smalest = statues[0]
    largest = statues[-1]
    
    for i in range(smalest, largest):
        if i not in statues:
            missing.append(i)
    
    return len(missing)