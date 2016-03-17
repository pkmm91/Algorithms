def cut_rod(p,n):
    """p is the list of prices, n is the length of the rod."""
    r = [0] * (n+1) # Holds the max revenue of each length
    s = [0] * (n+1)
    r[0] = 0
    for j in range(1,n+1):
        q = -1
        for i in range(1,j+1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r,s

def cut_rod_solution(p,n):
    r,s = cut_rod(p,n)
    while n > 0:
        print s[n]
        n -= s[n]

def main():
    p = [0,1,5,8,9,10,17,17,20,24,30]
    n = 8
    cut_rod_solution(p,n)

if __name__ == "__main__":
    main()
