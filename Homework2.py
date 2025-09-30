import math

#Bai1
# cd, cr = map(float,(input().split()))
# chu_vi= (cd+cr)*2
# dien_tich = cd*cr
# print(chu_vi)
# print(dien_tich)

#Bai2
# r=float(input())
# s = r**2*3.14
# p = 2*r*3.14
# print(s)
# print(p)

#Bai3
# a,b,c = map(float,input().split())
# p = (a+b+c)/2
# if(a+b<=c or a+c<=b or b+c<=a): print("Khong la 3 canh tam giac")
# elif(a+b>c and a+c>b and b+c>a):
#     if(a==b and b==c):
#         print("ĐỀU")
#         print("P=", 3*a)
#         print("S=", ((a**2)* math.sqrt(3))/4 )
#     elif(a==b or b==c or c==a):
#         print("CÂN")
#         print("P=", a+b+c)
#         print("S=", math.sqrt(p*(p-a)*(p-b)*(p-c)))
#     elif(a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2=b**2):
#         print("VUÔNG")
#         print("P=", a + b + c)
#         print("S=", math.sqrt(p * (p - a) * (p - b) * (p - c)))
#     else:
#         print("THƯỜNG")
#         print("P=", a + b + c)
#         print("S=", math.sqrt(p * (p - a) * (p - b) * (p - c)))

#Bai4
# a,b = map(float,input().split())
# if(a==0 and b!=0): print("Vo nghiem")
# if(a==0 and b==0): print("Vo so nghiem")
# else: print("Nghiem=", -b/a)

#Bai5
# a,b,c = map(float,input().split())
# delta = b**2 - 4*a*c
# if delta < 0: print("Vo nghiem")
# if(delta ==0): print("Nghiem duy nhat =",-b/2a)
# if(delta > 0):
#     print("Nghiem 1 =", (-b + math.sqrt(delta)/(2*a))
#     print("Nghiem 2 =", (-b - math.sqrt(delta)/(2*a))

#Bai6
# numbers = list(map(float,input().split()))
# print(max(numbers))

#Bai7
# numbers = list(map(float,input().split()))
# print(min(numbers))

#Bai8
# Giải hệ:
# ax + by = m
# cx + dy = n

# a, b, m = map(float, input("Nhập a, b, m: ").split())
# c, d, n = map(float, input("Nhập c, d, n: ").split())
#
# # Xét trường hợp đặc biệt
# if a == 0 and b == 0 and c == 0 and d == 0:
#     if m == 0 and n == 0:
#         print("Hệ có vô số nghiệm")
#     else:
#         print("Hệ vô nghiệm")
# else:
#     # Cố gắng giải theo cách thế
#     if a != 0:
#         # từ pt1: x = (m - b*y)/a
#         # thế vào pt2: c*((m - b*y)/a) + d*y = n
#         A = d - (c * b) / a   # hệ số của y
#         B = n - (c * m) / a   # hằng số còn lại
#
#         if A == 0:
#             if B == 0:
#                 print("Hệ có vô số nghiệm")
#             else:
#                 print("Hệ vô nghiệm")
#         else:
#             y = B / A
#             x = (m - b * y) / a
#             print(f"Hệ có nghiệm duy nhất: x = {x}, y = {y}")
#
#     elif c != 0:
#         # từ pt2: x = (n - d*y)/c
#         # thế vào pt1: a*((n - d*y)/c) + b*y = m
#         A = b - (a * d) / c
#         B = m - (a * n) / c
#
#         if A == 0:
#             if B == 0:
#                 print("Hệ có vô số nghiệm")
#             else:
#                 print("Hệ vô nghiệm")
#         else:
#             y = B / A
#             x = (n - d * y) / c
#             print(f"Hệ có nghiệm duy nhất: x = {x}, y = {y}")
#
#     else:
#         print("Không giải được bằng cách đơn giản")

#Bai9
# x = float(input())
# du_gio = x%3600
# gio = (x-du_gio)/3600
# x = x - gio*3600
# du_phut = x % 60
# phut = (x-du_phut)/60
# x = x - phut*60
# print (gio,"giờ", phut,"phút", x, "giây")

#Bai10
# x, y = map(float, input().split())
# r = float(input())
# x1, y1 = map(float, input().split())
# if(((x1-x)**2 + (y1-y)**2) == r**2): print("Thuộc đường tròn")
# else: print("Không thuộc đường tròn")

#Bai11
# x, y = map(float, input().split())
# print(x**y)