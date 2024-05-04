def solution(X, A):
    position_covered = set()
    
    for i in range(len(A)):
        position_covered.add(A[i])
        if len(position_covered) == X:
            return i
    return -1
    