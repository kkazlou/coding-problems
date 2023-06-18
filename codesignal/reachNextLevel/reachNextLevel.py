def solution(experience, threshold, reward):
    if experience + reward >= threshold:
        return True
    else:
        return False
