#W7A1
# def binary_search(arr, left, right, target):
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     return '-1'
#
# lst = list(map(int, input().split()))
# k = int(input())
# print(binary_search(lst, 0, len(lst)-1, k))

#W7A2
# def count_occurences(arr, x):
#     count = 0
#     for i in arr:
#         if i == x:
#             count += 1
#     return count
#
# lst = list(map(int, input().split()))
# k = int(input())
# print(count_occurences(lst, k))

#W7A3
# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-i-1):
#             if arr[j]> arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1, len(arr)):
#             if arr[min_index] > arr[j]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
#
# lst = list(map(int, input().split()))
# print()

#W7A4
#C1: Time O(n^2), space:O(1)
# def count_occurences(lst, x):
#     count = 0
#     for i in lst:
#         if i == x:
#             count += 1
#     return count
#
# lst = list(map(int, input().split()))
# max = 0
# for i in lst:
#     if count_occurences(lst, i) > max:
#         max = count_occurences(lst, i)
#
# for i in lst:
#     if count_occurences(lst, i) == max:
#         print(i,"xuat hien nhieu nhat, som nhat,", max, "lan")
#         break

#C2: time: O(n), space: O(n)
# lst = list(map(int, input().split()))
# fre = {}
#
# for i in lst:
#     if i not in fre:
#         fre[i] = 1
#     else:
#         fre[i] += 1
#
# max_fre = max(fre.values())
#
# for i in lst:
#     if fre[i] == max_fre:
#         print(i, "xuat hien nhieu nhat, som nhat,", max_fre, "lan")
#         break

#W7A5
# def count_pair(lst, k):
#     fre = {}
#     count = 0
#
#     for x in lst:
#         y = k - x
#         if y in fre:
#             count += fre[y]
#         if x not in fre:
#             fre[x] = 1
#         else:
#             fre[x] += 1
#
#     return count
#
# lst = list(map(int, input().split()))
# k = int(input())
# print(count_pair(lst, k))

#W7A6
# lst = input()
# lst = eval(lst) #chay chuoi thanh bat cu kieu du lieu nao trong giong
# flat = []
# for sub in lst:
#     for x in sub:
#         flat.append(x)
# print(flat)

#W7A7
# lst = eval(input())
# store = []
# for i in range (len(lst)):
#     store.append(1)
#
# for i in range(1,len(lst)):
#     for j in range(0, i):
#         if lst[i] > lst[j]:
#             store[i] = max(store[i], store[j]+1)
# longest_sub = max(store)
# print(longest_sub)

#W7A8
#C1: O(m*n)
# def shortest_interval(arr, k):
#     temp = []
#     interval = []
#     for i in range(len(arr)):
#         if arr[i][0] <= k and k <= arr[i][1]:
#             temp.append(arr[i])
#
#     if temp==[]:
#         return -1
#
#     for i in range(len(temp)):
#             interval.append(temp[i][1]-temp[i][0]+1)
#     return min(interval)
#
# lst = eval(input())
# queries = eval(input())
# storage = []
# for i in queries:
#     storage.append(shortest_interval(lst, i))
# print(storage)

#C2: O(NlogN + NlogM)
# def can_duoi(arr, k):
#     left = 0
#     right = len(arr)
#     while left < right:
#         mid = (left + right)//2
#         if arr[mid][0] >= k:
#             right = mid
#         else:
#             left = mid + 1
#     return left
#
# def can_tren(arr, k):
#     left = 0
#     right = len(arr)
#     while left < right:
#         mid = (left + right)//2
#         if arr[mid][0] > k:
#             right = mid
#         else:
#             left = mid + 1
#     return left
#
# intervals = eval(input())
# queries = eval(input())
# intervals = sorted(intervals, key=lambda x: x[1]-x[0]+1)
# result = [-1]*len(queries)
#
# queries_index = []
# for i in range(len(queries)):
#     queries_index.append((queries[i],i))
#
# for interval in intervals:
#     if queries_index == []:
#         break
#
#     l, r = interval[0], interval[1]
#     length = r - l+ 1
#     l = can_duoi(queries_index, l)
#     r = can_tren(queries_index, r)
#
#     for k in range(l, r):
#         temp = queries_index[k][1]
#         result[temp] = length
#
#     del queries_index[l : r]
# print(result)

#W7A11
# cau_van = input()
# tu_khoa = input()
# so_lan = cau_van.count(tu_khoa)
# print(so_lan)

# lst = input()
# key = input()
# count = 0
#
# len_lst = len(lst)
# len_key = len(key)
#
# for i in range(len_lst - len_key):
#     sub_string = lst[i:i + len_key]
#     if sub_string == key:
#         count +=1
# print(count)

#W7A12
# a = input()
# b = input()
# c = input()
# d = input()
# res = [(a,'A'),(b,'B'),(c,'C'),(d,'D')]
# res = sorted(res, key = lambda x:x[0])
# for i in range(len(res)):
#     print(res[i][1], end=" ")

#W7A13
# lst = list(map(int, input().split()))
# d = {}
# res = []
# for i in range (len(lst)):
#     if lst[i] not in d:
#         d[lst[i]] = 1
#     else:
#         d[lst[i]] += 1
# for key, value in d.items():
#     if (key+1) in d:
#         res.append(value + d[key+1])
# result = max(res)
# print(result)

#W7A14
# n = int(input())
# lst = list(map(int, input().split()))
# res = []
# for i in range(n-1,-1,-1):
#     if lst[i] == 7:
#         res.append(i)
# if res == []:
#     print("Not found")
# else:
#     print(*res)

#W7A15
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(input().strip())
#
# if lst[-1] == 'Nemo':
#     print(f"{lst[-2]} and {lst[0]}")
# elif lst[0] == 'Nemo':
#     print(f"{lst[-1]} and {lst[1]}")
# else:
#     for i in range(len(lst)):
#         if lst[i] == 'Nemo':
#             print(f"{lst[i-1]} and {lst[i+1]}")
#             break


