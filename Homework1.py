import math

# #Bai1
# n=int(input())3
# print(2*n)

# #Bai2
# a,b = map(float, input().split())
# print((a*b)-(a/2)**2*3.14)

#Bai3
# n = input()
# a=ord(n)
# if (65 <=a and a<=90):
#     print(chr(a+32))
# elif(97<=a and a<=122):
#     print(chr(a-32))

# n=input()
# print(n.swapcase())

# #Bai4
# c = input()
# if c.isdigit():
#     print("Là chữ số")
# elif c.isalpha():
#     print("Là alphabet")
# else:
#     print("ERROR")

#Bai5
# hoa = input()
# thuong = ord(hoa) +31
# if(thuong == 96):
#     print('`')
# else:
#     print(chr(thuong))

#Bai6
# a, b, c = map(float, input().split())
# if( a+b>c and b+c>a and c+a>b):
#     p = (a+b+c)/2
#     s = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print(f'{s:.1f}')
# else :
#     print("Khong phai 3 canh cua tam giac")

#Bai7
# n=input()
# print(n[4], n[8], sep=',')

#Bai8
# name=input("Ten chu ho:")
# n=int(input("Chi so thang truoc:"))
# m=int(input("Chi so thang nay:"))
# dung = m-n
# print("Ho va ten:", name)
# if 0<=dung<=50:print("Tien phai tra la:",int(1984*dung*1.08))
# elif 51<=dung<=100:print("Tien phai tra la:",int(2050*dung*1.08))
# elif 101<=dung<=200:print("Tien phai tra la:",int(2380*dung*1.08))
# elif 201<=dung<=300:print("Tien phai tra la:",int(2998*dung*1.08))
# elif 301<=dung<=400:print("Tien phai tra la:",int(3350*dung*1.08))
# elif dung>401: print("Tien phai tra la:",int(3460*dung*1.08))

#Mot so bai tap khac
#1
# n = int(input())
# if(n%2==0):
#     print("So chan")
# else:
#     print("So le")

#2
# n = int(input())
# if(n%10==5):
#     print("True")
# else:
#     print("False")

#3
# n = int(input())
# if(n%15==0):
#     print("True")
# else:
#     print("False")

#4
# n = int(input())
# if( n <18):
#     print("Chua du tuoi")
# else:
#     print("Du tuoi")

#5
# a, b  = map(int, input().split())
# if(a>b): print(a)
# elif(a==b): print("Bang nhau")
# else: print(b)

#6
# c = input()
# if c.isdigit():
#     print("Là chữ số")
# elif c.isalpha():
#     print("Là alphabet")

#7
# n = int(input())
# if(0<= n and n<5): print("Yeu")
# if(5<=n and n<6.5): print("Trung binh")
# if(6.5<=n and n<8): print("Kha")
# if(8<=n and n<=10): print("Gioi")

#8
# n = int(input())
# if(n%400==0): print("Nam nhuan")
# elif(n%4==0 and n%100!=0): print("Nam nhuan")
# else: print("Khong nam nhuan")

#9
# n = int(input())
# match n:
#     case 1: print("Mot")
#     case 2: print("Hai")
#     case 3: print("Ba")
#     case 4: print("Bon")
#     case 5: print("Nam")
#     case 6: print("Sau")
#     case 7: print("Bay")
#     case 8: print("Tam")
#     case 9: print("Chin")
#     case 0: print("Khong")

#10
# n = int(input())
# if (n>=4): print("Qua mon")
# else: print("Hoc lai")

#11
# n = int(input())
# check = 2025 - n
# if(check<18): print("Chua du tuoi")
# else: print("Du tuoi")




