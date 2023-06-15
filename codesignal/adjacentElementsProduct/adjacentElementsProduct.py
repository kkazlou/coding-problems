def solution(inputArray):

    product_max = inputArray[0] * inputArray[1]
    
    for i in range(len(inputArray) - 1):
        product = inputArray[i] * inputArray[i+1]
        
        if product > product_max:
            product_max = product
    
    return product_max
