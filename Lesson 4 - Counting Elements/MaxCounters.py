def solution(N, A):
    counters = [0] * N #number of numbers that are needed to be counted
    max_counter = 0 #Updating of our max_counter once encountered N + 1
    last_max = 0 
    
    
    for num in A:
        if 1 <= num <= N:
            if counters[num - 1] < last_max:
                counters[num - 1] = last_max
            counters[num - 1] += 1
            max_counter = max(max_counter, counters[num - 1])
            
        elif num >= N + 1:
            last_max = max_counter
    
    for i in range(N):
        if counters[i] < last_max:
            counters[i] += last_max
        
    return counters

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))