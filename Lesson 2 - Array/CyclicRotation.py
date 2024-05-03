def solution(A, K):
    
    #Checking if the A is empty
    if not A:
        return A
    
    K %= len(A)
    num_rotated = A[-K:] + A[:-K]
    return print(f"Rotated List:{num_rotated}")

num_inputs = int(input("Enter the number of inputs: "))
num_list = []

for i in range(num_inputs):
    user_input = input(f"{i + 1}. Enter Number: ")
    i + 1
    num_list.append(user_input)

num_rotation = int(input("Enter number of rotation/s: "))
print(f"Number/s entered: {num_list}")
solution(num_list, num_rotation)