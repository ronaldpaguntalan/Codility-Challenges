def solution(X, A):
    position_covered = set()
    
    
    for i in range(len(A)):
        position_covered.add(A[i])
        print(position_covered)
        if len(position_covered) == X:
            return i
    return -1

earliest_time = solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
print(earliest_time)