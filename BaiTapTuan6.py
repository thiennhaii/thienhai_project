#W6A1
# def xoa_lap():
#     lst = list(map(int, input().split()))
#     str = []
#     seen = set()
#     for i in lst:
#         if i not in seen:
#             str.append(i)
#             seen.add(i)
#     return str
# print(xoa_lap())

#W6A2
# def cumu_sum():
#     lst = list(map(int, input().split()))
#     lst_sum=[]
#     for i in range(len(lst)):
#         sum = 0
#         for j in range(i+1):
#             sum += lst[j]
#         lst_sum.append(sum)
#     return lst_sum
# print(cumu_sum())

# #W6A3
# def rotate():
#     tup = tuple(map(int, input().split()))
#     k = int(input())
#     lst = list(tup)
#     for i in range(k):
#         lst.append(lst[0])
#         lst.pop(0)
#     return lst
# print(rotate())

#W6A4
# def mapping():
#     mapp = {}
#     s=input().split()
#     for pair in s:
#         key, value = pair.split(":")
#         if key not in mapp:
#             mapp[key] = []
#         mapp[key].append(value)
#     return mapp
# print(mapping())

#W6A5
# def mapping():
#     lst = list(map(int, input().split()))
#     dict = {}
#     dict['positives'] = []
#     dict['negatives'] = []
#     dict['zeros'] = []
#     for i in lst:
#         if i > 0 and i not in dict['positives']:
#             dict['positives'].append(i)
#         if i < 0 and i not in dict['negatives']:
#             dict['negatives'].append(i)
#         if i == 0 and i not in dict['zeros']:
#             dict['zeros'].append(i)
#     return dict
# print(mapping())

#W6A6
# lst = list(map(int, input().split()))
# sum = 0
# for i in lst:
#     sum += i
# print(sum)

#W6A7
# def tup():
#     tup = tuple(map(int, input().split()))
#     lst = list(tup)
#     print(lst[0], lst[-1])
#     for i in range(len(lst)-1,0,-1):
#         lst.insert(len(lst)-1-i, lst[len(lst)-1])
#         lst.pop()
#     print(*tuple(lst))
# tup()

# #W6A8
# def count():
#     lst = list(input().split())
#     dict = {}
#     for str in lst:
#         if str not in dict:
#             dict[str] = 1
#         else:
#             dict[str] += 1
#     return dict
# print(count())

#W6A9
# def cong_dict():
#     lst1 = list(input().split())
#     lst2 = list(input().split())
#     dict1={}
#     dict2={}
#     dict0={}
#     for i in lst1:
#         if i not in dict1:
#             dict1[i]=1
#         else:
#             dict1[i]+=1
#     for i in lst2:
#         if i not in dict2:
#             dict2[i]=1
#         else:
#             dict2[i]+=1
#
#     dict1=dict(sorted(dict1.items()))
#     dict2=dict(sorted(dict2.items()))
#
#     dict0= dict1.copy()
#     for key, value in dict2.items():
#         if key not in dict0:
#             dict0[key]= value
#         else:
#             dict0[key]+= value
#
#     dict0 = dict(sorted(dict0.items()))
#     print (dict0)
# cong_dict()

#W6A11
# def sort_so():
#     tup = tuple(map(int, input().split()))
#     lst_chan = []
#     lst_le = []
#     lst = list(tup)
#     for x in lst:
#         if x%2==0:
#             lst_chan.append(x)
#         else:
#             lst_le.append(x)
#     tup_le = tuple(lst_le)
#     tup_chan = tuple(lst_chan)
#     print(tup_chan)
#     print(tup_le)
# sort_so()

#W6A12
# def check():
#     lst = list(map(int, input().split()))
#     dict0 = {}
#     for i in lst:
#         if i not in dict0:
#             dict0[i] = 1
#         else:
#             dict0[i] +=1
#     max_val = max(dict0.values())
#     min_key = min(key for key, value in dict0.items() if value == max_val)
#     return min_key
#
# print(check())

#W6A13
# def dao_nguoc():
#     lst = input().split()
#     dict0 = {}
#     for pair in lst:
#         key, value = pair.split(':')
#         dict0[value] = key
#     return dict0
# print(dao_nguoc())

#W6A14
# def so_chung():
#     lst1 = list(map(int, input().split()))
#     lst2 = list(map(int, input().split()))
#     lst0 = []
#
#     lst1 = set(lst1)
#     lst2 = set(lst2)
#
#     lst1 = sorted(lst1)
#     lst2 = sorted(lst2)
#
#     if len(lst1)<=len(lst2):
#         for i in lst1:
#             if i in lst2:
#                 lst0.append(i)
#     else:
#         for i in lst2:
#             if i in lst1:
#                 lst0.append(i)
#
#     return lst0
#
# print(so_chung())

#W6A15
# def sort_dict():
#     lst = input().split()
#     k = int(input())
#     dict0 = {}
#     new_dict = {}
#
#     for pair in lst:
#         key, value = pair.split(':')
#         dict0[key] = value
#
#     for key, value in dict0.items():
#         if int(value) > k:
#             new_dict[key] = value
#     return new_dict
# print(sort_dict())

# #W6A10
# def sum_k():
#     lst = list(map(int, input().split()))
#     k = int(input())
#     result = set()
#
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i] + lst[j] == k:
#                 result.add((min(lst[i],lst[j]), max(lst[i],lst[j])))
#
#     result = list(result)
#     result = sorted(result, key=lambda x: x[0])
#     return result
# print(sum_k())


