import math

from fontTools.misc.cython import returns

#Bai1
# for i in range(100):
#     if(i%2!=0): print(i)

#Bai2
# for i in range(100)
#     if(i%6==0): print(i)

#Bai3
# a=int(input())
# for i in range (1,10):
#     print(a,"*",i, "=", a*i)

#Bai4

#Bai5
# n=int(input())
# tong=n*(n+1)/2
# print(tong)

#Bai6
# n=int(input())
# for i in range(1, round(math.sqrt(n))):
#     if(n%i==0):
#         print(i, n/i)

#Bai7
# n=int(input())
# count=0
# for i in range(1, round(math.sqrt(n))):
#     if(n%i==0):
#         count+=1
# print(count*2)

#Bai8
# def uoc_chung(a, b)
#     g= math.gcd(a,b)
#     for i in range (1, int(math.sqrt(g))+1):
#         if(g%i == 0):
#             print(i)
#             if i != g//i:
#                 print g//i
#
# a, b = map(int, input().split())
# uoc_chung(a, b)

#Bai9
# a = int(input())
# if(int(math.sqrt(a))==math.sqrt(a)): print("True")
# else: print("False")

#Bai10
# n = int(input())
# tong=0
# for i in range(1, n):
#     if(n%i==0):
#         tong+=i
#
# if(tong==n): print("So hoan hao")
# else: print("Khong hoan hao")

#Bai11
# n = int(input())
# while(n<=0):
#     print("Nhap lai:")
#     n = int(input())
# print("Hop le:", n)

#Bai12
# n = int(input())
# if math.sqrt(2*n+0.25)-0.5 == int(math.sqrt(2*n+0.25)-0.5):
#     k = int(math.sqrt(2*n+0.25)-0.5)-1
# else:
#     k = int(math.sqrt(2*n+0.25)-0.5)
# print(k)

#Bai13
# n = int(input())
# k=0
# s=0
# while s<=n:
#     k+=1
#     s+= 1/k
# print(k)

#Bai14
# inf = float('inf')
# ne_inf = float('-inf')
# while True:
#     n = int(input())
#     if(n==-1):
#         break
#     if n < inf: inf = n
#     if n > ne_inf: ne_inf = n
# print(inf, ne_inf)\

#Bai15
# n = int(input())
# cnt=0
# while(n!=0):
#     n//=10
#     cnt+=1
# print(cnt)

#Bai16
# n = int(input())
# cnt_chan=0
# cnt_le=0
# while(n!=0):
#     if(n%2==0):
#         n = n // 10
#         cnt_chan+=1
#     elif(n%2==1):
#         n = n // 10
#         cnt_le+=1
# print(cnt_chan,cnt_le)

#Bai17
# n=int(input())
# s=0
# while(n!=0):
#     s+=n%10
#     n//=10
# print(s)

#Bai18
# n = int(input())
# ok = True
# while(n!=1):
#     if n %3!=0:
#         ok = False
#         break
#     else:
#         n = n // 3
# if ok:
#     print("La so 3^k")
# elif(n<=1):
#     print("Khong la so 3^k")
# else:
#     print("Khong la so 3^k")

#Bai19
# def fibonacci(num):
#     fib = [0, 1]
#     for i in range(2, num + 1):
#         fib.append(fib[i - 1] + fib[i - 2])
#     return fib[num]
# n = int(input())
# for i in range(0,n+5):
#     if(fibonacci(i) > n ):
#         print(fibonacci(i-1))
#         break

#Bai20
# def nguyen_to(num):
#     if num<2: return False
#     for i in range(2, int(math.sqrt(num))+1):
#         if num%i == 0: return False
#     return True
#
# n = int(input())
# cnt=0
# while n!=0:
#     check = n%10
#     if nguyen_to(check):
#         cnt+=1
#     n = n//10
# print(cnt)
