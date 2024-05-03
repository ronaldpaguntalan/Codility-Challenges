def solution(X, Y, D):
    
    distance = Y - X
    jumps = distance // D
    
    if distance % D != 0:
        jumps += 1
    return jumps

pos_x = int(input('Enter Starting Position: '))
pos_y = int(input('Enter Target Last Position: '))
step_d = int(input('Enter the number of distance per Jump: '))

print(solution(pos_x, pos_y, step_d))
