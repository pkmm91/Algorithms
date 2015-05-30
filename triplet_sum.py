def triplet_sum(input1,input2,input3):
    new_input = sorted(input1)
    for i in xrange(input2-1):
        l = i + 1
        r = input2 - 1
        while l < r:
            if (new_input[i] + new_input[l] + new_input[r]) == input3:
                return True
            elif (new_input[i] + new_input[l] + new_input[r]) < input3:
                l +=1
            else:
                r -=1
    return False
print triplet_sum([1 , 3 , 12 , 4], 4 , 14)
                
                
