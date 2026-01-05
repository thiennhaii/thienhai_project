import math
# #W8A1
# class Cyclinder:
#     def __init__(self, radius, height):
#         self.radius = radius
#         self.height = height
#
#     def Surface(self):
#         self.surface = self.radius ** 2 * 3.14 * 2 + self.radius * self.height * 3.14 * 2
#         return f"Surface = {self.surface:.2f}"
#
#     def Volume(self):
#         self.volume = self.radius ** 2 * 3.14 * self.height
#         return f"Volume = {self.volume:.2f}"
#
# radius, height = map(float, input().split())
#
# result = Cyclinder(radius, height)
# print(result.Surface())
# print(result.Volume())

#W8A2
# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def is_leap_year(self):
#         if self.year % 400 == 0:
#             return True
#         elif self.year % 4 == 0 and self.year % 100 != 0:
#             return True
#         else:
#             return False
#
#     def is_valid_date(self):
#         if self.month < 1 or self.month > 12:
#             return False
#
#         if self.year < 1:
#             return False
#
#         days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#         if self.is_leap_year():
#             days[1] = 29
#
#         if self.day < 1 or self.day > days[self.month-1]:
#             return False
#
#         return True
#
#     def next_day(self):
#         days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#         if self.month == 2 and self.is_leap_year():
#             max_day = 29
#         else:
#             max_day = days[self.month-1]
#
#         if self.day < max_day:
#             self.day += 1
#         else:
#             self.day = 1
#             if self.month < 12:
#                 self.month += 1
#             else:
#                 self.month = 1
#                 self.year += 1
#         return self
#
#     def __str__(self):
#         return f"{self.day:02d}/{self.month:02d}/{self.year:02d}"
#
# day, month, year = map(int, input().split('/'))
# date = Date(day, month, year)
# if date.is_valid_date() == False:
#     print("INVALID")
# else:
#     date = date.next_day()
#     print(str(date))

#W8A3
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def is_origin(self):
#         if self.x == 0 and self.y ==0:
#             return True
#         else:
#             return False
#
#     def is_x_axis(self):
#         if self.y ==0:
#             return True
#         else:
#             return False
#
#     def is_y_axis(self):
#         if self.x == 0:
#             return True
#         else:
#             return False
#
#     def distance_to_origin(self):
#         dist = math.sqrt(self.x**2 + self.y**2)
#         return f"{dist:.2f}"
#
#     def __str__(self):
#         if self.is_origin():
#             return (
#                 "La goc toa do \n"
#                 f"Distance to origin: {self.distance_to_origin()}"
#             )
#         elif self.is_x_axis():
#             return (
#                 "Nam tren truc x \n"
#                 f"Distance to origin: {self.distance_to_origin()}"
#             )
#         elif self.is_y_axis():
#             return (
#                 "Nam tren truc y \n"
#                 f"Distance to origin: {self.distance_to_origin()}"
#             )
#         else:
#             return f"Distance to origin: {self.distance_to_origin()}"
#
# x, y = map(float, input().split())
# position = Point(x, y)
# print(str(position))

#W8A4
# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def add(self):
#         return self.num1 + self.num2
#
#     def subtract(self):
#         return self.num1 - self.num2
#
#     def product(self):
#         return self.num1 * self.num2
#
#     def divide(self):
#         if self.num2 == 0:
#             return ("Invalid operation")
#         return self.num1 / self.num2
#
#     def power(self):
#         return self.num1 ** self.num2
#
#     def mod(self):
#         if self.num2 == 0:
#             return ("Invalid operation")
#         return self.num1 % self.num2
#
#     def set_numbers(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#
# num1, num2 = map(float, input().split())
# calc = Calculator(num1, num2)
#
# while True:
#     print("MENU")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Product")
#     print("4. Divide")
#     print("5. Power")
#     print("6. Mod")
#     print("7. Set Numbers")
#
#     choice = input("Choose operation: ")
#     if choice == "1":
#         print(calc.add())
#
#     elif choice == "2":
#         print(calc.subtract())
#
#     elif choice == "3":
#         print(calc.product())
#
#     elif choice == "4":
#         print(calc.divide())
#
#     elif choice == "5":
#         print(calc.power())
#
#     elif choice == "6":
#         print(calc.mod())
#
#     elif choice == "7":
#         num1, num2 = map(float, input().split())
#         calc.set_numbers(num1, num2)
#
#     else:
#         print("Invalid operation")
#
#     exit = input("Do you want to exit?")
#     if exit.lower() == "yes":
#         break
#     elif exit.lower() == "no":
#         continue

#W8A5
# class ShoppingCart:
#     def __init__(self):
#         self.items = []
#
#     def add_item(self, name, price):
#         self.items.append({'name': name, 'price': price})
#
#     def delete_item(self, name):
#         for item in self.items:
#             if item['name'] == name:
#                 self.items.remove(item)
#
#     def check_empty(self):
#         return len(self.items) == 0
#
#     def total_price(self):
#         total = 0
#         for item in self.items:
#             total += item['price']
#         return total
#
#     def show_items(self):
#         if len(self.items) !=0:
#             for item in self.items:
#                 print(item['name'])
#         else:
#             print("NONE")
#
#     def clear(self):
#         self.items = []
#
# cart = ShoppingCart()
# while True:
#     print("MENU")
#     print("2. Add item")
#     print("3. Delete item")
#     print("4. Check empty")
#     print("5. Total price")
#     print("6. Show items")
#     print("7. Clear")
#
#     choice = input("Enter your choice: ")
#     if choice == "2":
#         name = input("Item name: ")
#         price = float(input("Item price: "))
#         cart.add_item(name, price)
#
#     elif choice == "3":
#         name = input("Item name: ")
#         cart.delete_item(name)
#
#     elif choice == "4":
#         print(cart.check_empty())
#
#     elif choice == "5":
#         print("Total price: ", cart.total_price())
#
#     elif choice == "6":
#         cart.show_items()
#
#     elif choice == "7":
#         cart.clear()
#
#     exit = input("Do you want to exit? ")
#     if exit.lower() == "yes":
#         break
#     elif exit.lower() == "no":
#         continue

#W8A6
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def scale(self, k):
#         self.width *= k
#         self.height *= k
#
#     def Area(self):
#         area = self.width * self.height
#         return f"Area: {area:.2f}"
#
#     def Perimeter(self):
#         perimeter = 2 * (self.width + self.height)
#         return f"Perimeter: {perimeter:.2f}"
#
# width,height, k = map(float, input().split())
# result = Rectangle(width, height)
# result.scale(k)
# print(result.Area())
# print(result.Perimeter())

#W8A7
# class Fraction:
#     def __init__(self, num, den):
#         self.num = num
#         self.den = den
#         g = math.gcd(num, den)
#         self.num //= g
#         self.den //= g
#         if self.den < 0:
#             self.den = -self.den
#             self.num = -self.num
#
#     def add(self, other):
#         num = int(self.den * other.num + self.num * other.den)
#         den = int(self.den * other.den)
#         g = math.gcd(num, den)
#         num = num //g
#         den = den //g
#         return(
#             f"{num}/{den}"
#         )
#
#     def sub(self, other):
#         num = int(self.num * other.den - self.den * other.num)
#         den = int(self.den * other.den)
#         g = math.gcd(num, den)
#         num = num //g
#         den = den //g
#         return(
#             f"{num}/{den}"
#         )
#
#     def mul(self, other):
#         num = int(self.num * other.num)
#         den = int(self.den * other.den)
#         g = math.gcd(num, den)
#         num = num //g
#         den = den //g
#         return(
#             f"{num}/{den}"
#         )
#
#     def div(self, other):
#         num = int(self.num * other.den)
#         den = int(self.den * other.num)
#         g = math.gcd(num, den)
#         num = num //g
#         den = den //g
#         return(
#             f"{num}/{den}"
#         )
#
# a, b, op, c, d = input().split()
# num1 = Fraction(int(a), int(b))
# num2 = Fraction(int(c), int(d))
#
# if op == "+":
#     print(num1.add(num2))
# elif op == "-":
#     print(num1.sub(num2))
# elif op == "*":
#     print(num1.mul(num2))
# elif op == "/":
#     print(num1.div(num2))

#W8A8
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             return 0
#         else:
#             self.balance -= amount
#
#     def __str__(self):
#         return f"{self.balance:.2f}"
#
# owner, initial_balance = input().split()
# initial_balance = float(initial_balance)
# bank_account = BankAccount(owner, initial_balance)
# n = int(input())
# while n > 0:
#     choice = input().split()
#     if choice[0] == "DEPOSIT":
#         bank_account.deposit(float(choice[1]))
#     elif choice[0] == "WITHDRAW":
#         bank_account.withdraw(float(choice[1]))
#     n -= 1
# print(str(bank_account))

#W8A9
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.score = {}
#
#     def add(self, subject, score):
#         self.score[subject] = score
#
#     def average(self):
#         total = 0
#         for score in self.score.values():
#             total += score
#         Average = total / len(self.score.keys())
#         return Average
#
#     def rank(self):
#         if self.average() >=8:
#             return "Excellent"
#         elif self.average() < 8 and self.average() >=6.5:
#             return "Good"
#         elif 5 <= self.average() < 6.5:
#             return "Average"
#         else:
#             return "Poor"
#
# name = input()
# student = Student(name)
# n = int(input())
# while n > 0:
#     subject, score = input().split()
#     student.add(subject, float(score))
#     n-=1
# average = student.average()
#
# print(f"{name} {average:.2f} {student.rank()}")

#W8A10
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add(self, book):
#         self.books.append(book)
#
#     def count_author(self, author):
#         count = 0
#         for book in self.books:
#             if book.author == author:
#                 count += 1
#         return count
#
#     def count_year(self, year):
#         count = 0
#         for book in self.books:
#             if book.year == year:
#                 count += 1
#         return count
#
# n = int(input())
# library = Library()
# while n > 0:
#     choice = input()
#     parts = choice.split()
#     if parts[0] == "ADD":
#         data = parts[1]
#         info = data.split(';')
#         title = info[0]
#         author = info[1]
#         year = int(info[2])
#         book = Book(title, author, year)
#         library.add(book)
#
#     elif parts[0] == "COUNT":
#         print(library.count_author(parts[1]))
#
#     elif parts[0] == "COUNTYEAR":
#         print(library.count_year(int(parts[1])))
#
#     n-=1

#W8A11
# class Coordinate:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def vector(self, other):
#         x = other.x - self.x
#         y = other.y - self.y
#         z = other.z - self.z
#         return Coordinate(x, y, z)
#
#     def scalar_product(self, other):
#         return (self.x * other.x + self.y * other.y + self.z * other.z)
#
#     def cross_product(self, other):
#         x = self.y * other.z - self.z * other.y
#         y = self.z * other.x - self.x * other.z
#         z = self.x * other.y - self.y * other.x
#         return Coordinate(x, y, z)
#
#     def length_vector(self):
#         return math.sqrt(self.x**2 + self.y**2 + self.z**2)
#
# xA, yA, zA = map(float, input().split())
# xB, yB, zB = map(float, input().split())
# xC, yC, zC = map(float, input().split())
# xD, yD, zD = map(float, input().split())
#
# A = Coordinate(xA, yA, zA)
# B = Coordinate(xB, yB, zB)
# C = Coordinate(xC, yC, zC)
# D = Coordinate(xD, yD, zD)
#
# AB = A.vector(B)
# AC = A.vector(C)
# cross_product_ABC = AB.cross_product(AC)
# BC = B.vector(C)
# BD = B.vector(D)
# cross_product_BCD = BC.cross_product(BD)
#
# num = cross_product_ABC.scalar_product(cross_product_BCD)
# den = cross_product_ABC.length_vector() * cross_product_BCD.length_vector()
# result = math.acos(abs(num / den))
# result = math.degrees(result)
# print(f"{result:.2f}")

#W8A12
# class ComplexNumber:
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary
#
#     def mul(self, other):
#         real = self.real * other.real - self.imaginary * other.imaginary
#         imaginary = self.real * other.imaginary + self.imaginary * other.real
#         return ComplexNumber(real, imaginary)
#
#     def __str__(self):
#         return f"{self.real} {self.imaginary}"
#
# realA, ImaginaryA = map(int, input().split())
# realB, ImaginaryB = map(int, input().split())
#
# A = ComplexNumber(realA, ImaginaryA)
# B = ComplexNumber(realB, ImaginaryB)
#
# result = A.mul(B)
# print(str(result))

#W8A13
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_valid(self):
#         if self.a + self.b <= self.c or self.b + self.c <= self.a or self.c + self.a <= self.b:
#             return False
#         return True
#
#     def area(self):
#         p = (self.a + self.b + self.c) / 2
#         result = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
#         return result
#
#     def __str__(self):
#         return f"{self.area():.2f}"
#
# a, b, c = map(int, input().split())
# triangle = Triangle(a, b, c)
# if triangle.is_valid() == False:
#     print("invalid")
# else:
#     if triangle.area() == int(triangle.area()):
#         print(int(triangle.area()))
#     else:
#         print(str(triangle))
#

