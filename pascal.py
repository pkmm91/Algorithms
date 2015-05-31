def pascal(n):
    row = [1]
    for k in range(n):
        row.append(row[k] * (n-k) / (k + 1))
    return row
print pascal(input())
