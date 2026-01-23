import os
import math
import struct


#W11A1
# def reverse(path: str) -> str:
#     try:
#         with open(path, 'r') as f:
#             content = f.read()
#         reversed_content = content[::-1]
#         return(int(reversed_content))
#     except FileNotFoundError:
#         print("File Not Found")
#         return 0
#     except ValueError:
#         print("Not integer")
#         return 0
#
# filename = "number.txt"
# test_value = input()
# with open(filename, 'w') as f:
#     f.write(test_value)
# result = reverse(filename)
# print(result)
# os.remove(filename)

#W11A2
# def canWinNim(path:str) -> bool:
#     try:
#         with open(path, 'r') as f:
#             content = f.read()
#             if int(content) % 4 == 0:
#                 return False
#             return True
#
#     except FileNotFoundError:
#         print("File not Found")
#         return 0
#     except ValueError:
#         print("Value Error")
#         return 0
#
# filename = "canWinNim.txt"
# number = input()
# with open(filename, 'w') as f:
#     f.write(number)
# if canWinNim(filename):
#     print("True")
# else:
#     print("False")
# os.remove(filename)

#W11A3
# def housesOfHogwarts(path: str):
#     try:
#         with open(path, 'r') as f:
#             content = f.readlines()
#             for i in range(len(content)):
#                 print(content[i].strip())
#     except:
#         print("Wrong name")
#         return 0
#
# filename = "hogwars.txt"
# n = int(input())
# with open(filename, 'w') as f:
#     for i in range(n):
#         f.write(input() + '\n')
# housesOfHogwarts(filename)
# os.remove(filename)

#W11A4
# def areAnagrams(path1: str, path2: str):
#     try:
#         str1 = {}
#         str2 = {}
#         with open(path1, 'r') as f1:
#             content1 = f1.read().strip()
#             for letter in content1.lower():
#                 if letter.isalpha():
#                     if letter not in str1:
#                         str1[letter] = 1
#                     else:
#                         str1[letter] += 1
#         with open(path2, 'r') as f2:
#             content2 = f2.read().strip()
#             for letter in content2.lower():
#                 if letter.isalpha():
#                     if letter not in str2:
#                         str2[letter] = 1
#                     else:
#                         str2[letter] += 1
#         if str1 == str2:
#             return True
#         return False
#     except FileNotFoundError:
#         print("File not exist")
#
# filename1 = "String1.txt"
# filename2 = "String2.txt"
# with open(filename1, 'w') as f1:
#     f1.write(input())
# with open(filename2, 'w') as f2:
#     f2.write(input())
#
# if areAnagrams(filename1, filename2):
#     print("True")
# else:
#     print("False")
# os.remove(filename1)
# os.remove(filename2)

# #W11A5
# def count(path: str, character: str):
#     try:
#         with open(path, 'r') as f:
#             content = f.read()
#         cnt = 0
#         for letter in content:
#             if letter == character:
#                 cnt += 1
#         return cnt
#     except FileNotFoundError:
#         print("File Not Found")
#         return 0
#
# filename = "countLetter.txt"
# with open(filename, 'w') as f:
#     f.write(input())
# character = input()
# print(count(filename, character))
# os.remove(filename)

#W11A6
# def count(path: str, character: str):
#     try:
#         with open(path, 'r') as f:
#             content = f.read()
#         cnt = 0
#         for letter in content.lower():
#             if letter == character:
#                 cnt += 1
#         return cnt
#     except FileNotFoundError:
#         print("File Not Found")
#         return 0
#
# filename = "countLetter.txt"
# with open(filename, 'w') as f:
#     f.write(input())
# character = input()
# print(count(filename, character))
# os.remove(filename)

#W11A7
# path = input()
# if os.path.exists(path):
#     print("YES")
# else:
#     print("NO")

#W11A8
# def fibonacci(path:str):
#     try:
#         with open(path, 'r') as f:
#             num = int(f.read())
#         lst = ['a','b']
#         for i in range(2,num+1):
#             lst.append(lst[i-1]+lst[i-2])
#         for i in range(len(lst)):
#             print(f"f({i}) = {lst[i]}")
#
#     except FileNotFoundError:
#         print("File not exist")
#
# filename = "fibonacci.txt"
# n = input()
# with open(filename, 'w') as f:
#     f.write(n)
# fibonacci(filename)
# os.remove(filename)

#W11A9
# def grade10(path:str):
#     try:
#         with open(path, 'r') as f:
#             lines = f.readlines()
#
#         for i in range(1, len(lines)):
#             data = lines[i].strip().split(',')
#             if len(data)>=6:
#                 ho = data[1]
#                 ten = data[2]
#                 diem_thcs4 = data[5]
#                 if diem_thcs4 == '10':
#                     print(f"{ho} {ten}")
#     except FileNotFoundError:
#         print("File not exist")
#
# filename = "sinhvien.csv"
# n = int(input("Nhap so luong:"))
# with open(filename, 'w') as f:
#     f.write("STT, Ho, Ten, Ngay sinh, Dai so, THCS4, THCS1\n")
#     for i in range(1, n+1):
#         row = input()
#         f.write(row + "\n")
# grade10(filename)
# os.remove(filename)

#W11A10
# def getMoney(path: str) -> list[int]:
#     with open(path, 'r') as f:
#         houses = [int(x) for x in f.read().split()]
#         return houses
#
# def rob(houses: list[int]) -> int:
#     if not houses:
#         return 0
#     if len(houses) == 1:
#         return houses[0]
#
#     dp = [houses[0]]
#     dp[1] = max(houses[0], houses[1])
#     for i in range(2, len(houses)):
#         dp.append(max(dp[i - 2] + houses[i], dp[i - 1]))
#     return max(dp)
#
#
# filename = "money.txt"
# with open(filename, 'w') as f:
#     f.write(input())
#
# houses = getMoney(filename)
# print(rob(houses))
# os.remove(filename)

#W11A11
# def number(path: str):
#     try:
#         with open(path, 'r') as f:
#             content = f.read().split()
#             numbers = [int(x) for x in content]
#             val_max = max(numbers)
#             val_min = min(numbers)
#             return f"{val_max} {val_min}"
#     except:
#         print("Mission failed")
#         return None
#
# filename = "numbers.txt"
# link = input()
# result = number(link)
# if result is not None:
#     print(result)

#W11A12
# def maximumProduct(path: str) -> int:
#     try:
#         with open(path, 'r') as f:
#             content = f.read().split()[1:]
#             content = sorted(content)
#             res1 = int(content[-1]) * int(content[-2]) * int(content[-3])
#             res2 = int(content[0] * content[1] * content[-1])
#             result = max(res1, res2)
#             return result
#     except FileNotFoundError:
#         print("File Not Found")
#         return 0
#
# filename = "maxProduct.txt"
# with open(filename, 'w') as f:
#     n = input()
#     f.write(n + '\n')
#     f.write(input())
#
# print(maximumProduct(filename))
# os.remove(filename)

#W11A13
# def moveZeroes(path: str):
#     try:
#         with open(path, 'r') as f:
#             content = f.read().split()[1:]
#         temp = []
#         store_zero = []
#         for num in content:
#             if num == '0':
#                 store_zero.append(num)
#             else:
#                 temp.append(num)
#         res = temp + store_zero
#         res = [int(x) for x in res]
#         return res
#
#     except FileNotFoundError:
#         print("File Not Found")
#         return 0
#
# filename = "moveZeeroes.txt"
# with open(filename, 'w') as f:
#     f.write(input() + '\n')
#     f.write(input())
# print(moveZeroes(filename))
# os.remove(filename)

#W11A14
# def averageTime(path: str):
#     try:
#         with open(path, 'r') as f:
#             content = f.readlines()
#             sum = 0
#             for i in range(1, len(content)):
#                 data = content[i].split(',')
#                 sum += float(data[1])
#             res = sum / (len(content) - 1)
#             return float((f"{res:.2f}"))
#     except FileNotFoundError:
#         print("File not exist")
#         return 0
#
# filename = "averageTime.txt"
# with open(filename, 'w') as f:
#     f.write("Lap, Time\n")
#     while True:
#         choice = input()
#         if choice == "end":
#             break
#         else:
#             f.write(choice + '\n')
# print(averageTime(filename))
# os.remove(filename)

#W11A15
# def findMovies(path: str):
#     try:
#         with open(path, 'r') as f:
#             content = f.readlines()
#             res = []
#             for i in range(1, len(content)):
#                 data = content[i].strip().split(',')
#                 if data[2] != "boring" and float(data[3]) >= 8.0:
#                     res.append(data[1].strip())
#             return res
#     except FileNotFoundError:
#         print("File Not Found")
#         return 0
#
# filename = "findMovies.txt"
# with open(filename, 'w') as f:
#     f.write("id, movie, description, rating\n")
#     while True:
#         choice = input()
#         if choice == "end":
#             break
#         else:
#             f.write(choice + "\n")
# res = findMovies(filename)
# for movie in res:
#     print(movie)
# os.remove(filename)

#W11A16
# def perimeter(path: str):
#     try:
#         with open(path,'r') as f:
#             content = f.readlines()
#             data = [x.strip() for x in content if x.strip()]
#             res = []
#             for i in range(0, len(data), 2):
#                 shape_line = data[i]
#                 peri = data[i+1]
#                 shape_type = shape_line.strip().split(':')
#                 if shape_type[1].strip() == "SQUARE":
#                     side = peri.strip().split(':')
#                     p = 4*float(side[1])
#                     res.append(f"{p:.2f}")
#                 elif shape_type[1].strip() == "RECTANGLE":
#                     side = peri.split()
#                     p = (2*float(side[1]) + 2*float(side[3]))
#                     res.append(f"{p:.2f}")
#                 elif shape_type[1].strip() == "CIRCLE":
#                     side = peri.strip().split(':')
#                     p = 3.14*2*float(side[1])
#                     res.append(f"{p:.2f}")
#             return res
#     except FileNotFoundError:
#         print("File Not Found")
#         return 0
#
# filename = "perimeter.txt"
# with open(filename,'w') as f:
#     while True:
#         choice = input()
#         if choice == "end":
#             break
#         else:
#             f.write(choice + '\n')
# res = perimeter(filename)
# for i in res:
#     print(i)
# os.remove(filename)

#W11A17
# def productExceptSelf(path: str):
#     try:
#         with open(path, 'r') as f:
#             content = f.readlines()
#             data = content[1].split()
#             data = [int(i) for i in data]
#             res = []
#             for i in range(len(data)):
#                 res.append(math.prod(data[:i]) * math.prod(data[i+1:]))
#             return res
#     except FileNotFoundError:
#         print("File Not Found")
#         return 0
#
# filename = "ProductOfArrayExceptSelf.txt"
# with open(filename, 'w') as f:
#     f.write(input() + '\n')
#     f.write(input())
#
# res = productExceptSelf(filename)
# print(*res)
# os.remove(filename)

#W11A18
# def estimatedTime(path: str):
#     try:
#         with open(path, 'r') as f:
#             content = f.readlines()
#             src = content[0].split()
#             dest = content[1].split()
#             velo = content[2].split()
#             dist = math.sqrt((float(dest[2])-float(src[2]))**2 + (float(dest[4])-float(src[4]))**2)
#             time = dist/float(velo[1])
#             return float(f"{time:.2f}")
#     except FileNotFoundError:
#         print("File Not Found")
#         return 0
#
# filename = "estimatedTime"
# with open(filename, 'w') as f:
#     f.write(input()+"\n")
#     f.write(input()+"\n")
#     f.write(input())
# res = estimatedTime(filename)
# print(res)
# os.remove(filename)

#W11A19
# def round_num(path:str):
#     try:
#         with open(path, 'rb') as f:
#             data = f.read()
#             size = 8
#             res = []
#             for i in range(0, len(data), size):
#                 chunk = data[i:i+size]
#                 if len(chunk) == size:
#                     number = struct.unpack('d', chunk)[0]
#                     res.append(f"{number:.5f}")
#             return res
#     except ValueError:
#         print("ValueError")
#         return 0
#     except FileNotFoundError:
#         print("FileNotFoundError")
#         return 0
#
# link = input()
# user_input = input().split()
# with open(link, 'wb') as f:
#     for x in user_input:
#         binary_data = struct.pack('d', float(x))
#         f.write(binary_data)
# res = round_num(link)
# print(*res)
# os.remove(link)

#W11A120
# def imageSmoother(path: str):
#     try:
#         with open(path, 'r') as f:
#             lines = f.readlines()
#             # Lọc các dòng trống và chuyển thành ma trận số nguyên
#             data = [[int(x) for x in line.split()] for line in lines if line.strip()]
#
#             if not data:
#                 return
#
#             # Dòng đầu tiên là M
#             M = data[0][0]
#             # Các dòng tiếp theo là pixels.
#             # Dùng data[1:M+1] để đảm bảo lấy đúng M dòng dữ liệu ảnh
#             matrix = data[1:M + 1]
#
#             result = [[0] * M for _ in range(M)]
#
#             for r in range(M):
#                 for c in range(M):
#                     total_sum = 0
#                     count = 0
#                     # Quét vùng 3x3 quanh điểm (r, c)
#                     for i in range(r - 1, r + 2):
#                         for j in range(c - 1, c + 2):
#                             if 0 <= i < M and 0 <= j < M:
#                                 total_sum += matrix[i][j]
#                                 count += 1
#                     result[r][c] = total_sum // count
#
#             # In kết quả
#             for row in result:
#                 print(*(row))
#
#     except FileNotFoundError:
#         print("File Not Found")
#     except Exception as e:
#         print(f"Lỗi xử lý: {e}")
#
#
# # --- HÀM MAIN NHẬP TỪ BÀN PHÍM ---
# if __name__ == "__main__":
#     filename = "user_image.txt"
#
#     try:
#         print("Nhập kích thước M:")
#         m_input = input().strip()
#         if not m_input:
#             exit()
#         M = int(m_input)
#
#         print(f"Nhập ma trận {M}x{M} (nhập từng dòng hoặc dán cả cụm):")
#         with open(filename, 'w') as f:
#             f.write(f"{M}\n")
#             # Đọc đúng M dòng dữ liệu
#             for _ in range(M):
#                 row_data = input()
#                 f.write(row_data + "\n")
#
#         print("\n--- KẾT QUẢ ---")
#         imageSmoother(filename)
#
#     except ValueError:
#         print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
#     finally:
#         if os.path.exists(filename):
#             os.remove(filename)