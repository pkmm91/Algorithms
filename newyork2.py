def encode( p,  k,  s):
    l = []
    for i in range(k):
        new_str = ''
        for j in range(len(p)):
            new_str += s[p[j]-1]
        s = new_str
        l.append(s)
    print l[len(l)-1]
print encode([2 , 3 , 1] , 100000000 , 'tom')
