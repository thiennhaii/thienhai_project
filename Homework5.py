# W6A19
# lst=[]
# lst = list(map(int,input().split()))
# lst.sort()
# print(lst[-1])

#W6A20
# lst=[]
# while True:
#     n = input()
#     if n == "": break
#     lst.append(int(n))
# k = int(input())
# for index, value in enumerate(lst):
#     if value == k:
#         print(index)
#         break
# else: print("-1")

#W6A21
# lst=[]
# while True:
#     n = input()
#     if n =="": break
#     lst. append(n)
# for index, value in enumerate(lst):
#     print(index, value)

#W6A22
# def nhap_so():
#     return list(map(int, input().split()))
# day_so = nhap_so()
# print(max(day_so))

#W6A23
# n = int(input())
# def xoa_so():
#     lst = list(map(int, input().split()))
#     i = 0
#     while i < len(lst):
#         if lst[i] < n:
#             lst.pop(i)
#         else:
#             i = i + 1
#     return lst
# print(xoa_so())

#W6A24
# def sort_0():
#     lst = list(map(int, input().split()))
#     for i in range(len(lst)):
#         if lst[i] == 0:
#             lst.insert(0, 0)
#             lst.pop(i+1)
#     return lst
#
# print(sort_0())

#W6A25
# def check():
#     lst = list(map(int, input().split()))
#     str = []
#     for i in range(10):
#         if i not in lst:
#             str.append(i)
#     return str
# print(check())

#W6A26
# def local_sum():
#     lst = list(map(int, input().split()))
#     sum = 0
#     for i in range (1, len(lst)-1):
#         if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
#             sum+=lst[i]
#     return sum
# print(local_sum())

#W6A27
# n = int(input())
# def find():
#     lst = list(map(int, input().split()))
#     str = []
#     for index, value in enumerate(lst):
#         if value < n:
#             str.append(index)
#     if len(str) == 0:
#         return -1
#     else:
#         return str
# print(find())

#W6A28
# def check():
#     lst = list(map(int, input().split()))
#     lst_thuan = sorted(lst)
#     lst_dao = sorted(lst, reverse = True)
#     if len(lst) != len(set(lst)):
#         return ("Vo danh")
#     elif lst_thuan == lst:
#         return("Tang thuc su")
#     elif lst_dao == lst:
#         return("Giam thuc su")
#     else:
#         return("Vo danh")
# print(check())

#W6A16
# n, m = map(int, input().split())
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(f"{f'a{i}{j}'}", end ="    ")
#     print()

#W6A17
# n = int(input())
# for i in range(1, n+1):
#     cheo_chinh = f"a{i}{i}"
#     print(cheo_chinh, end = " ")
# print()
# for i in range(1, n+1):
#     cheo_phu = f"a{i}{n-i+1}"
#     print(cheo_phu, end = " ")

#W6A18
# n, m, k = map(int, input().split())
#
# print("Hang k:")
# for i in range(1, m+1):
#     print(f"a{k}{i}", end=" ")
# print()
#
# print("Cot k:")
# for i in range(1, n+1):
#     print(f"a{i}{k}", end=" ")



