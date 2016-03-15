words = ['zebra' , 'dog' , 'duck' , 'dot']
d = {}
for w in words:
    node = d
    for c in w:
        if c in node:
            counter , child = node[c]
            node[c] = (counter+1 , child)
        else:
            node[c] = (1 , {})
        node = node[c][1]
for w in words:
    node = d
    prefix = ''
    for c in w:
        prefix += c
        if node[c][0] == 1:
            break
        node = node[c][1]
    print prefix
