import math

#W4A1
# n = int(input())
# tong=0
# for i in range(1,n+1):
#     tong=tong+i
# print(tong)

#W4A2
# def nguyento(n):
#     if(n<2): return False
#     for i in range (2, int(math.sqrt(n))+1):
#             if(n%i==0):
#                 return False
#     return True
#
# n = (int(input()))
# while n<=0:
#     n = int(input())
# if nguyento(n):
#     print("So nguyen to")
# else:
#     print("Khong la so nguyen to")

#W4A3
# n = int(input())
# print(math.factorial(n))

#W4A4
# n = int(input())
# cnt=0
# while(n!=0):
#     n=n//10
#     cnt+=1
# print(cnt)

#W4A5
# n = int(input())
# lst=[]
# for i in range(n):
#     i = int(input())
#     lst.append(i)
# if 42 in lst:
#     print("True")
# else: print("False")

#W4A6
# n = int(input())
# def nguyento(n):
#         if(n<2): return False
#         for i in range (2, int(math.sqrt(n))+1):
#             if(n%i==0):
#                 return False
#         return True
#
# for i in range(n):
#     a, b = map(int, input().split())
#     tong=0
#
#
#     for i in range(a, b+1):
#         if(nguyento(i)): tong+=i
#     print(tong)

#W4A7
# n = int(input())
# ngto=0
# def nguyento(n):
#         if(n<2): return False
#         for i in range (2, int(math.sqrt(n))+1):
#             if(n%i==0):
#                 return False
#         return True
#
# if(nguyento(n)):
#     print(n)
# elif(nguyento(n)==False):
#     for i in range(1,n+1):
#         if(n%i==0 and nguyento(i)): ngto=i
#     print(ngto)

#W4A8
# def reverse(num):
#     temp=0
#     while(num>0):
#         temp=temp*10 + num%10
#         num=num//10
#     return temp
#
# n = int(input())
# cnt=0
# while(n != reverse(n)):
#     n = n + reverse(n)
#     cnt+=1
# print(cnt, n)

#W4A9
# def chinh_phuong(num):
#     if(int(math.sqrt(num)) == math.sqrt(num)): return True
#     else: return False
#
# def diff_num(num):
#     if num ==0:
#         return True
#     else:
#         lst9=[]
#         while(num>0):
#             chu_so = num%10
#             lst9.append(chu_so)
#             num = num//10
#
#         if(len(lst9)==1):
#             return True
#         elif(len(lst9)>1):
#             for i in range(len(lst9)):
#                 for j in range(i+1,len(lst9)):
#                     if(lst9[i]==lst9[j]): return False
#             return True
#
# n = int(input())
# lst9_2 = []
# for i in range(n+1):
#     if( chinh_phuong(i)== True and diff_num(i) == True):
#         lst9_2.append(i)
# if (lst9_2 == []): print("No number")
# else: print(*lst9_2) # * như để mở list ra và in các số mà không có dấu []

#Bai10
# def collatz(num):
#     cnt1=0
#     cnt2=0
#     while(num != 1):
#         if num % 2 == 0:
#             num = num / 2
#             cnt1+=1
#         else:
#             num = num * 3 + 1
#             cnt2+=1
#     cnt = cnt1+cnt2
#     return cnt+1
#
# n = int(input())
# storage = {}
# lst = []
# for i in range(1,n+1):
#     storage[i] = collatz(i)
# max_value = max(storage.values())
#
# for key, value in storage.items():
#     if(value==max_value):
#         lst.append(key)
# min_key=min(lst)
# print(min_key, max_value)

#Bai11
# n = int(input())
# cnt=0
# if(n%2==0):
#     for i in range(2,int(n/2)+1,2):
#         if(n%i==0):
#             cnt+=1
#     cnt=cnt+1
# else:
#     for i in range(2,int(n/2)+1,2):
#         if(n%i==0):
#             cnt+=1
# print(cnt)

#Bai12
# x, n = map(int, input().split()))
# print(x*(1.007**n))

#Bai13
# def tong_uoc(num):
#     nua_duoi = 0
#     nua_tren = 0
#     for i in range(1,int(math.sqrt(num))+1):
#         if num % i == 0:
#             nua_duoi += i
#             nua_tren += num//i
#     tong = nua_duoi + nua_tren - num
#     return tong
#
# a, b = map(int, input().split())
# if(tong_uoc(a) == b and tong_uoc(b) == a):
#     print("True")
# else:
#     print("False")

#Bai14
# def ucln(num1, num2):
#     du = 0
#     while (num1 != 0 and num2 != 0):
#         du = num1 % num2
#         num1 = num2
#         num2 = du
#     return num1
#
# m,n=map(int,input().split())
# if( m > n ): print(ucln(m,n))
# elif(m < n): print(ucln(n,m))
# else: print(m)

#Bai15
# def tim_ga_cho(tong_con, tong_chan):
#     if tong_chan % 2 != 0 or tong_con < 0 or tong_chan < 0:
#         return "invalid"
#
#     if tong_chan < tong_con * 2 or tong_chan > tong_con * 4:
#         return "invalid"
#
#     so_cho = (tong_chan // 2) - tong_con
#     so_ga = tong_con - so_cho
#
#     if so_ga < 0 or so_cho < 0:
#         return "invalid"
#
#     return f"Số gà: {so_ga}, Số chó: {so_cho}"
#
# tong_con_input = int(input("Nhập tổng số con: "))
# tong_chan_input = int(input("Nhập tổng số chân: "))
# ket_qua = tim_ga_cho(tong_con_input, tong_chan_input)
# print(ket_qua)