def solution(A):
    
    seen = set()
    
    for num in A: 
        if num in seen or num > len(A):
            return 0
        seen.add(num)
        
    if len(seen) == len(A):
        return 1
    else:
        return 0