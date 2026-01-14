import math
#W7A16
# lst = list(map(int, input().split()))
# d = {}
# res = []
# for i in lst:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
#
# for key, value in d.items():
#     if key < int(value):
#         res.append(int(value)-key)
#     elif key > int(value):
#         res.append(int(value))
#
# if len(res) == 0:
#     print("YES")
# else:
#     print("NO", sum(res))

#W7A17
# lst = list(map(int, input().split()))
# k = len(lst)//2
# res = 0
# count = 0
# for i in lst:
#     if count == 0:
#         res = i
#         count = 1
#     elif i == res:
#         count +=1
#     elif i != res:
#         count -=1
#
# if lst.count(res) > k:
#     print(res)
# else:
#     print(-1)

#W7A18
# lst = list(map(int, input().split()))
# chan = []
# le = []
# for i in lst:
#     if i % 2 == 0:
#         chan.append(i)
#     else:
#         le.append(i)
#
# chan = sorted(chan)
# le = sorted(le, reverse=True)
# for i in chan:
#     print(i)
# for i in le:
#     print(i)

#7A19
# lst1 = list(map(int, input().split()))
# lst2 = list(map(int, input().split()))
# res = []
# i, j = 0, 0
# while i< len(lst1) and j < len(lst2):
#     if lst1[0] < lst1[-1]:
#         if lst1[i] <= lst2[j]:
#             res.append(lst1[i])
#             i += 1
#         else:
#             res.append(lst2[j])
#             j += 1
#     else:
#         if lst1[i] >= lst2[j]:
#             res.append(lst1[i])
#             i += 1
#         else:
#             res.append(lst2[j])
#             j += 1
#
# res.extend(lst1[i:])
# res.extend(lst2[j:])
# print(*res)

#W7A20
# lst = list(map(str, input().split()))
# k = int(input())
# res = 0
# for x in lst:
#     if len(x)==k:
#         res += int(x)
# print (res)

#W7A21
# day, month = map(int, input().split())
# days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# res = 0
# if month < 1 or month > 12:
#     print("invalid")
# elif day < 1 or day > days_in_month[month - 1]:
#     print("invalid1")
# else:
#     res = day + sum(days_in_month[:month-1])
#     print(res)

#W7A22
# n = int(input())
# d = {}
# res = []
# for i in range(n):
#     name = input().split()
#     if name[-1] not in d:
#         d[name[-1]] = 1
#     else:
#         d[name[-1]] += 1
#
# max_freq = max(d.values())
# res = min(k for k,v in d.items() if v == max_freq)
# print(res)

# W7A23
# sentence = list(map(str, input().split()))
# count = 0
# for i in range(len(sentence)):
#     if len(sentence[i]) > 2 and sentence[i][0].isupper() == True and sentence[i][1:].islower() == True:
#         count+=1
# print(count)

#W7A24
# sentence = list(map(str, input().split()))
# res = []
# for i in range(0,len(sentence)):
#     if res == []:
#         res.append(sentence[i])
#     elif sentence[i] != res[-1]:
#         res.append(sentence[i])
#
# print(*res)

#W7A25
# numbers = input()
# k = int(input())
# start = 0
# remain = k
# res = ""
# for j in range(k):
#     max_idx = start
#     for i in range(start, len(numbers)- remain + 1):
#         if numbers[i] > numbers[max_idx]:
#             max_idx = i
#     res += numbers[max_idx]
#     remain -=1
#     start = max_idx + 1
# print(res)

# #W7A26
# string = input().strip()
# res = []
# num = ""
# for i in range(len(string)):
#     if string[i].isdigit():
#         num += string[i]
#     elif string[i].isalpha():
#         if num!= "":
#             res.append(int(num))
#             num = ""
# if num != "":
#     res.append(int(num))
#
# total = 0
# average = 0
# total = sum(res)
# average = total / len(res)
# if int(average) != average:
#     print(total, f"{average:.2f}")
# else:
#     print(total, int(average))

#W7A27
# string = input().strip()
# stack = {
#         '}':'{',
#         ']':'[',
#         ')':'(',
#         '>':'<'
# }
# check = []
# for i in string:
#     if i in stack.values():
#         check.append(i)
#     elif i in stack.keys():
#         if not check:
#             print("NO")
#             exit()
#         if stack[i] == check[-1]:
#             check.pop()
#         else:
#             print("NO")
#             exit()
# if not check:
#     print("YES")
# else:
#     print("NO")

#W7A28
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0:
#             return False
#     return True
#
# n = int(input())
# prime = []
# length_between_prime = {}
#
# for i in range(2,n+1):
#     if is_prime(i):
#         prime.append(i)
#
# for i in range(len(prime)-1):
#     length_between_prime[(prime[i], prime[i+1])] = prime[i+1] - prime[i]
# length_between_prime[(prime[-1],n)] = n - prime[-1]
#
# max_val = max(length_between_prime.values())
# for key, value in length_between_prime.items():
#     if value == max_val:
#         for i in range(key[0] +1, key[1]):
#             print(i, end = " ")
#         exit()

#W8A29
# lst = list(map(int, input().split()))
# length = [1]*len(lst)
# for i in range(len(lst)-1):
#     if lst[i+1] >= lst[i]:
#         length[i+1] = length[i] + 1
#     else:
#         length[i+1] = 1
#
# idx = 0
# max_length = max(length)
# for i in range(len(length)):
#     if length[i] == max_length:
#         idx = i
#         break
#
# for i in range((idx - (max_length - 1)), idx+1):
#     print(lst[i], end = " ")

#W8A30
# lst = list(map(int, input().split()))
# length = [1]*len(lst)
# res = []
#
# for i in range(1, len(lst)):
#     for j in range(i):
#         if lst[i] >= lst[j]:
#             length[i] = max(length[i], length[j]+1)
#
# max_length = max(length)
# for i in range(len(length)):
#     if length[i] == max_length:
#         idx = i
#         break
#
# for i in range(idx, -1, -1):
#     if length[i] == max_length:
#         res.append(lst[i])
#         max_length -= 1
#
# res.reverse()
# print(*res)

#W8A31
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
#
