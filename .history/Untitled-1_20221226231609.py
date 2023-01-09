# import itertools
# # 1
# def sum_a(n,b:list):
#     s = sum(b[n-1])+sum(b[0])
#     for i in b:
#         s+=i[0]+i[-1]
#     return s

# def sum_b(n,b:list):
#     return sum(
#         b[i][j]
#         for i, j in itertools.product(range(n), range(n))
#         if i == j or i + j == n - 1
#     )

# # def sum_d(n,b:list):



# print("a)  ",sum_a(4,[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))

# print("\nb)  ",sum_b(5,[
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5]]))


# # 2
# def oxiridan_oldingi(file_name):
#     with open(file_name,'r') as f:
#         satrlar=f.readlines()
#         return satrlar[-2]

# print(oxiridan_oldingi('Untitled-1.txt'))
        
# # 3
# class Vector:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
    
#     def uzunligi(self):
#         a=self.x
#         b=self.y
#         c=self.z
#         return (a*a+b*b+c*c)**0.5


# vek1=Vector(1,2,3)
# vek2=Vector(4,5,6)

# def qoshsh():
#     return (vek1.x+vek2.x,vek1.y+vek2.y,vek1.z+vek2.z)

# def ayrsh():
#     return (vek1.x-vek2.x,vek1.y-vek2.y,vek1.z-vek2.z)

# def skalyar_kop():
#     return vek1.x*vek2.x+vek1.y*vek2.y+vek1.z*vek2.z



# print(f"vek1+vek2 = {qoshsh()}")
# print(f"vek1-vek2 = {ayrsh()}")
# print(f"vek1*vek2 = {skalyar_kop()}")
# print(f"vek1 uzunligi {vek1.uzunligi()}")
# print(f"vek2 uzunligi {vek2.uzunligi()}")
# print(f"bek1 va vek2 orasidagi cos = {skalyar_kop()/(vek1.uzunligi()*vek2.uzunligi())}")


son,k=map(int,input().split())
sonlar = sorted(map(int ,str(son)))
print(sonlar)
