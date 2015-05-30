def maxstack(s):
    maxh , r , h = [] , [] , []
    for e in s:
        maxh.append(e[1])
        h.append(e[1])
        r.append(e[0])
    j = 0
    for i in xrange(1 , len(s)):
       for j in xrange(0 , i):
            if (r[i] < r[j]) and (h[i] < h[j]):
                maxh[i] = maxh[j] + h[i]
            
    max = -1
    for i in xrange(len(maxh)):
        if (max < maxh[i]):
            max = maxh[i]
    return max
    
t = int(raw_input())
for i in xrange(t):
    a = []
    num = int(raw_input())
    for i in xrange(num):
        arr = map(int , raw_input().split())
        a.append([arr[0] , arr[1]])
    k = sorted(a)
    print maxstack(k[::-1])
        
