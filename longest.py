def find_longest_palonodramic(s , i , l):
    if l == 1:
        return l
    if l == 0:
        return l
    if s[i] == s[i + l - 1]:
        return 2 + find_longest_palonodramic(s , i + 1,  l -2)
    else:
        return max(find_longest_palonodramic(s , i+1 , l-1) , find_longest_palonodramic(s , i , l-1) )

string = 'GEEKSFORGEEKS'
l = len(string)
print find_longest_palonodramic(list(string) , 0 ,  l)
