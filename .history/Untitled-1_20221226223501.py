import itertools
def sum_a(n,b:list):
    s = sum(b[n-1])+sum(b[0])
    for i in b:
        s+=i[0]+i[-1]
    return s

def sum_b(n,b:list):
    return sum(
        b[i][j]
        for i, j in itertools.product(range(n), range(n))
        if i == j or i + j == n - 1
    )


print("a)  ",sum_a(4,[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
print("b)  ",sum_b(4,[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))

