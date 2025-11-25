import math
#W5A1
# def Max_of_Two(a,b):
#     if a>b:
#         print(a)
#     else:
#         print(b)
# n,m = map(int, input().split())
# Max_of_Two(n,m)

#W5A2
# def swap(a,b):
#     c = a
#     a = b
#     b = c
#     print(a,b)
# n, m = map(int,input().split())
# swap(n,m)

#W5A3
# def prime(n):
#     if n < 2: return False
#     for i in range(2, int(math.sqrt(n)) ):
#         if n % i == 0:
#             return False
#     return True
# n = int(input())
# if prime(n): print("So nguyen to")
# else: print("Hop so")

#W5A4
# def perfect_num(num):
#     sum = 0
#     for i in range(1,num):
#         if num%i==0: sum += i
#     return sum
# n = int(input())
# if perfect_num(n) == n:
#     print("So hoan hao")
# else:
#     print("Khong")

#W5A5
# lst = []
# flag = False
# while True:
#     n = int(input())
#     if n == -1:
#         break
#     lst.append(n)
# k = int(input())
# for i in range(len(lst)):
#     if k == lst[i]:
#         flag = True
#         print(i)
# if flag == False:
#     print("-1")

#W5A6
# def factorial(n):
#     temp = 1
#     if n == 0: return 0
#     for i in range(1, n+1):
#         temp *= i
#     return temp
# n = int(input())
# print(factorial(n))

#W5A7
# def casio(num1, num2, operator):
#     if operator == "-":
#         return f"{(num1 - num2):.2f}"
#     elif operator == "+":
#         return f"{(num1 + num2):.2f}"
#     elif operator == "*":
#         return f"{(num1 * num2):.2f}"
#     elif operator == "/":
#         return f"{(num1 / num2):.2f}"
# num1, num2 = map(float, input().split())
# operator = input()
# print(casio(num1, num2, operator))

#W5A8
# def hamming(num1, num2):
#     num1 = str(f"{num1:b}")
#     num2 = str(f"{num2:b}")
#     temp1 = len(num1)
#     temp2 = len(num2)
#     count = 0
#     if len(num1) > len(num2):
#         num2 = "0"*(len(num1)-len(num2)) + num2
#     else:
#         num1 = "0"*(len(num2)-len(num1)) + num1
#     for i in range(len(num1)):
#         if num1[i] != num2[i]:
#             count+=1
#     print(count)
# n,m = map(int,input().split())
# print(n,m)

#Cach2: DUNG XOR

#W5A9
# def sum_digit(num):
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     return sum
# n = int(input())
# print(sum_digit(n))

#W5A10
# def marking_index(s):
#     storage = {}
#     index_store = []
#     for index, char in enumerate(s):
#         if char not in storage:
#             storage[char] = index
#         else:
#             index_store.append(storage[char])
# 
# def iso_linear(str1, str2):
#     if len(str1) != len(str2):
#         return False
#     else:
#         return marking_index(str1) == marking_index(str2)
#
# str1, str2 = input().split()
# if iso_linear(str1, str2):
#     print("True")
# else:
#     print("False")