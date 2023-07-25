def solution(sequence):
    count = 0
    maximum = -1000000          # edge case
    previous_maximum = -1000000 # edge case
    for s in sequence:
        if s > maximum:
            # Sequence is increasing
            previous_maximum = maximum
            maximum = s
        elif s > previous_maximum:
            # Violation - remove current maximum outlier
            count += 1
            maximum = s
        else:
            # Violation - remove current item outlier
            count += 1
        if count > 1:
            return False
    return True