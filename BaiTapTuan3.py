#W3A2
# a, b = map(int, input().split())
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print ( a,b)

#W3A3
# n = int(input())
# if(n & (n-1)==0): print("Luy thua cua 2")
# else: print("Khong la luy thua")

#W3A4
# m, n = map(float, input().split())
# print ( int(m/n))

#W3A5
# m, n = map(float, input().split())
# print ( (int(m/n))+1)

#W3A6
# n = int(input())
# if(n&1==0): print ("Chẵn")
# else: print("Lẻ")

#W3A7
# a, b = map(int, input().split())
# if( a <  0 and b < 0 ): print("YES")
# else: print("NO")

#W3A8
# a, b = input().split()
# if( len(a)> len(b)): print("True")
# else: print("False")

#W3A9
# a,b,c = map(int,input().split())
# if(a+b> c and b+c>a and c+a>b): print("YES")
# else: print("NO")

#W3A10
# numbers = list(map(int,input().split()))
# print(max(numbers))

#W3A11
# a,b,c = map(int,input().split())
# if(a+b> c and b+c>a and c+a>b):
#     if(a==b==c): print("ĐỀU")
#     elif(a==b and a==c or b==c and b==a or c==b and c==a): print("CÂN")
#     else: print("THƯỜNG")
# else: print("KHÔNG PHẢI TAM GIÁC")

#W3A12
# n = int(input())
# if( n%4==0 and n%100!=0): print("YES")
# elif(n%400==0): print("YES")
# else: print("NO")

#W3A14
# a, b = map(float, input().split())
# if( a==0 and b!=0): print("Vô nghiệm")
# elif(a==0 and b==0): print("Vô số nghiệm")
# else: print(f'{-b/a:.2f}')

#W3A15
# n = float(input())
# if (n>=8): print("Gioi")
# elif(n>=6.5 and n < 8): print("Kha")
# elif(n>=5 and n< 6.5): print("Trung binh")
# elif(n<5): print("Yeu")

#W3A16
# n = float(input())
# nguyen_xuong = n // 1
# nguyen_len = nguyen_xuong + 1
# print(nguyen_xuong)
# print(nguyen_len)
# if(n>=0):
#     print ( (n+0.5)//1)
# else:
#     x = n - 0.5
#     x = x // 1
#     print(x+1)

#W3A17
# a,b,c,d= map(float,input().split())
# t = b/a
# if( b*t == c):
#     if(c*t==d): print("Cap so nhan")
#     else: print("Khong la cap so nhan")
# else: print("Khong la cap so nhan")



