def nextGreater(array):
    c = len(array)*[-1]
    b = []
    for index, value in enumerate(array):
        if len(b) > 0:
            top_element = b[-1]
	    top_element_index = top_element[0]
	    top_element_value = top_element[1]
	    while top_element_value < value and len(b) > 0:
                c[top_element_index] = value
                b.pop()
                if len(b) > 0:
                    top_element = b[-1]
                    top_element_index = top_element[0]
                    top_element_value = top_element[1]
                else:
                    break
        b.append((index , value))
    return c
     
print nextGreater([6, 7, 4, 3, 5, 2])
