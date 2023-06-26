def solution(value1, weight1, value2, weight2, maxW):
    current_value = 0
    
    # pick up both items
    if weight1 + weight2 <= maxW:
        weight1 + weight2
        current_value = value1 + value2
        
        return current_value
        
    # pick up item1    
    if weight1 <= maxW:
        current_value = value1
    
    # pick up item2    
    if weight2 <= maxW:
        if value2 >= current_value:
           current_value = value2
    
    return current_value
