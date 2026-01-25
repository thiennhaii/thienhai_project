#W9A1
# lst1 = list(map(int, input().split()))
# lst2 = list(map(int, input().split()))
# merge_lst = []
# i, j = 0, 0
# while i < len(lst1) and j < len(lst2):
#     if lst1[i] < lst2[j]:
#         merge_lst.append(lst1[i])
#         i += 1
#     else:
#         merge_lst.append(lst2[j])
#         j += 1
# merge_lst.extend(lst1[i:])
# merge_lst.extend(lst2[j:])
# print(*merge_lst)

#W9A2
# matrix = []
# while True:
#     try:
#         line = input().strip()
#         row = list(map(int, line.split()))
#         matrix.append(row)
#     except EOFError:
#         break
# n = int(input())
# k = 1
# for i in range(len(matrix[0])):
#     for j in range(len(matrix)):
#         if k == n:
#             print(matrix[i][j])
#         k += 1

#W9A3
# number = list(input().strip())
# swap = []
# idx_min = 0
# res = ""
#
# for i in range(len(number)):
#     min_val = "10"
#     for j in range(len(number) - 1, i, -1):
#         if number[j] < number[i] and number[j] < min_val:
#             min_val = number[j]
#
#     if min_val != "10":
#         for k in range(len(number) - 1, i, -1):
#             if number[k] == min_val:
#                 idx_min = k
#                 break
#         swap.extend([i, idx_min])
#         break
#
# if not swap:
#     if len(number) >= 2:
#         number[-1], number[-2] = number[-2], number[-1]
# else:
#     number[swap[0]], number[swap[1]] = number[swap[1]], number[swap[0]]
#
# for i in range(len(number)):
#     res += str(number[i])
# print(int(res))

#W9A4
# def check():
#     a = input().strip()
#     b = input().strip()
#     n,m = len(a),len(b)
#     dp = []
#     for i in range(n+1):
#         row = []
#         for j in range(m+1):
#             row.append(False)
#         dp.append(row)
#
#     dp[0][0] = True
#     for i in range(n):
#         for j in range(m+1):
#             if dp[i][j] == True:
#                 if j<m and a[i].upper()==b[j]:
#                     dp[i+1][j+1] = True
#                 if a[i].islower():
#                     dp[i+1][j] = True
#
#     if dp[n][m] == True:
#         print("YES")
#     else:
#         print("NO")
#
# n = int(input())
# for i in range(n):
#     check()

#W9A5
# lst1 = list(map(int, input().split()))
# lst2 = list(map(int, input().split()))
# flag = False
# for i in range(len(lst2)-len(lst1)+1):
#     if lst2[i:i+len(lst1)] == lst1:
#         flag = True
#         break
# if flag:
#     print("YES")
# else:
#     print("NO")

"Bài khó quá cho em cheat 1 tí từ đoạn này cho kịp giờ lam coding system ah"

#W9A6
# import sys
#
#
# def solve():
#     # Đọc dữ liệu nhanh bằng sys.stdin
#     input_data = sys.stdin.read().split()
#     if not input_data:
#         return
#
#     n = int(input_data[0])
#     a = list(map(int, input_data[1:]))
#
#     # Bước 1: Tìm điểm gãy i từ phải sang trái
#     # (Vị trí đầu tiên mà a[i] < a[i+1])
#     i = n - 2
#     while i >= 0 and a[i] >= a[i + 1]:
#         i -= 1
#
#     if i >= 0:
#         # Bước 2: Tìm số a[j] lớn hơn a[i] một chút ở bên phải i
#         j = n - 1
#         while a[j] <= a[i]:
#             j -= 1
#
#         # Bước 3: Tráo đổi a[i] và a[j]
#         a[i], a[j] = a[j], a[i]
#
#     # Bước 4: Đảo ngược đoạn từ i + 1 đến hết dãy
#     # (Nếu i = -1, tức là dãy đang giảm dần, nó sẽ đảo thành dãy tăng dần đầu tiên)
#     left = i + 1
#     right = n - 1
#     while left < right:
#         a[left], a[right] = a[right], a[left]
#         left += 1
#         right += 1
#
#     # In kết quả
#     print(*(a))
#
#
# if __name__ == "__main__":
#     solve()

#W9A7
# def canPlaceFlowers(flowerbed, k):
#     count = 0
#     n = len(flowerbed)
#
#     for i in range(n):
#         # Kiểm tra xem ô hiện tại có trống không
#         if flowerbed[i] == 0:
#             # Kiểm tra hàng xóm bên trái
#             # (Nếu là ô đầu tiên i==0 thì coi như bên trái trống)
#             left_empty = (i == 0) or (flowerbed[i - 1] == 0)
#
#             # Kiểm tra hàng xóm bên phải
#             # (Nếu là ô cuối cùng i==n-1 thì coi như bên phải trống)
#             right_empty = (i == n - 1) or (flowerbed[i + 1] == 0)
#
#             # Nếu cả hai bên đều trống, ta trồng hoa!
#             if left_empty and right_empty:
#                 flowerbed[i] = 1  # Trồng hoa vào đây
#                 count += 1  # Tăng số lượng hoa đã trồng
#
#                 # Nếu đã đủ số hoa k thì dừng luôn cho nhanh
#                 if count >= k:
#                     return True
#
#     return count >= k
#
# # Ví dụ chạy thử:
# # flowerbed = [1, 0, 0, 0, 1], k = 1 -> True (Trồng vào giữa: 1, 0, 1, 0, 1)
# # flowerbed = [1, 0, 0, 0, 1], k = 2 -> False

#W9A8
# def is_path_crossing(moves):
#     # Tọa độ hiện tại của rô-bốt
#     x, y = 0, 0
#
#     # Lưu trữ các vị trí đã đi qua dưới dạng tuple (x, y)
#     # Dùng set để tìm kiếm với tốc độ O(1)
#     visited = {(0, 0)}
#
#     for move in moves:
#         # Cập nhật tọa độ dựa trên lệnh di chuyển
#         if move == 'U':
#             y += 1
#         elif move == 'D':
#             y -= 1
#         elif move == 'R':
#             x += 1
#         elif move == 'L':
#             x -= 1
#
#         # Kiểm tra xem vị trí mới này đã từng được ghé thăm chưa
#         new_pos = (x, y)
#         if new_pos in visited:
#             return True
#
#         # Nếu chưa, thêm vào danh sách đã đi qua
#         visited.add(new_pos)
#
#     return False
#
# # Ví dụ chạy thử:
# # moves = "NES" (Lên, Phải, Xuống) -> False
# # moves = "NESWW" (Lên, Phải, Xuống, Trái, Trái) -> True (quay lại 0,0)

#W9A9
# def Median(nums):
#     a, b, c, d, e = nums
#
#     # Lần lượt thực hiện các phép so sánh cố định
#     if a > b: a, b = b, a  # 1
#     if c > d: c, d = d, c  # 2
#     if a > c:  # 3 (Đưa cặp nhỏ hơn về phía a, b)
#         a, c = c, a
#         b, d = d, b
#
#     # Bây giờ a là số nhỏ nhất trong 4 số (a, b, c, d)
#     a = e  # Thay a bằng số cuối cùng e
#
#     if a > b: a, b = b, a  # 4
#     if a > c:  # 5 (Đưa số nhỏ hơn về phía a)
#         a, c = c, a
#         b, d = d, b
#
#     # Bây giờ trung vị sẽ là số nhỏ hơn trong b và c
#     if b < c:  # 6
#         return b if b > d else min_of_two(b, d)  # Phần này cần return b hoặc c/d

# #W9A10
# def findRadius_TwoPointers(houses, heaters):
#     houses.sort()
#     heaters.sort()
#
#     r = 0
#     j = 0  # Con trỏ cho heaters
#
#     for i in range(len(houses)):
#         # Trong khi lò sưởi tiếp theo (j+1) đứng gần ngôi nhà i hơn lò sưởi hiện tại (j)
#         # thì ta dịch con trỏ lò sưởi lên.
#         while j < len(heaters) - 1 and \
#                 abs(heaters[j + 1] - houses[i]) <= abs(heaters[j] - houses[i]):
#             j += 1
#
#         # Cập nhật bán kính r là khoảng cách đến lò sưởi gần nhất đã tìm được
#         r = max(r, abs(heaters[j] - houses[i]))
#
#     return r