def running_sum(A):
    running_sum = []
        
    for i in range(len(A)):
        if len(running_sum) == 0:
            running_sum.append(A[i])
            continue
            
        running_sum.append(A[i] + running_sum[-1])

    return running_sum
            
def solution(A):
        
    run_sum = running_sum(A)
        
    min_diff = 999999
        
    for i in range(len(run_sum) - 1):
        this_diff = abs(run_sum[i] - (run_sum[-1] - run_sum[i]))
        if this_diff < min_diff:
            min_diff = this_diff
        
    return min_diff

A = [3,1,2,4,3]
running_sum(A)

print(f"The absolute minimum difference is {solution(A)}")
        
