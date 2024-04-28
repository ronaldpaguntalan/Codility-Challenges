def solution(N):
    
    value = "{0:b}".format(N)

    accumulated = 0
    maxGap = 0 
    
    for i in value:
        if i == "0":
            accumulated += 1
        elif i == "1":
            if accumulated >  maxGap:
                maxGap = accumulated
            accumulated = 0
    return maxGap

number = int(input("Enter a number: "))
binaryGap = solution(number)
print(f"The largest binary gap is {binaryGap}")