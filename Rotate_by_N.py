arr = map(int , raw_input().split())
k = int(raw_input())
l = len(arr)
reverse_arr = arr[::-1]
A ,B  = reverse_arr[:k] , reverse_arr[k:l]
print A[::-1] + B[::-1]
