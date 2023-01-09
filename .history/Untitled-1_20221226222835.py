n=int(input())


def sum_a(n,b:list):
    s = sum(b[n-1])+sum(b[0])
    for i in b:
        s+=i[0]+i[-1]
    return s



