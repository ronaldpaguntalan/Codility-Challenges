def solution(A):
    A.sort()
    
    for i in range(0, len(A), 2):
        if i == len(A) - 1 or A[i] != A[i+1]:
            return A[i]
        
listArray = [2,1,2,1,4,5,7,4,5]
print(solution(listArray))