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

# def sum_d(n,b:list):



# print("a)  ",sum_a(4,[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))

# print("\nb)  ",sum_b(5,[
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5]]))



def oxiridan_oldingi(file_name):
    with open(file_name,'r') as f:
        satrlar=f.readlines()
        return satrlar[-2]

# print(oxiridan_oldingi('Untitled-1.txt'))
        


