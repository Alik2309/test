# def test(lst):
#     lst1=[]
#     cnt=0
#     for i in lst:
#         if i!=0:
#             lst1.append(i)
#         else:
#             cnt+=1 
#     lst1.extend([0]*cnt)
#     return lst1
# a=[3, 4, 0, 0, 2, 0, 6, 7, 8, 0, 0, 9, 10, 7, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# print(test(a))

# def test(lst):
#     maxx=lst[0]
#     sum=0
#     for i in lst[0]:
#         sum+=i
#     for j in lst:
#         cnt=0
#         for i in j:
#             cnt+=i
#         if cnt>sum:
#             sum=cnt
#             maxx=j
#     return maxx
# a=[[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# print(test(a))

# def test(lst):
#     cnt=len(lst)//3
#     cnt1=lst[:cnt]
#     cnt2=lst[cnt:cnt*2]
#     cnt3=lst[cnt*2:]
#     print("Chunk 1", cnt1)
#     print("After reversing it", cnt1[::-1])
#     print("Chunk 2", cnt2)
#     print("After reversing it", cnt2[::-1])
#     print("Chunk 3", cnt3)
#     print("After reversing it", cnt3[::-1])
# a=[11, 45, 8, 23, 14, 12, 78, 45, 89]
# test(a)

# def test(lst):
#     dct={}
#     for i in lst:
#         if i in dct:
#             dct[i]+=1
#         else:
#             dct[i] = 1
#     return dct
# a=[11, 45, 8, 11, 23, 45, 23, 45, 89]
# print(test(a))

# def test(lst):
#     text={}
#     for i in lst:
#         if i in text:
#             text[i]+=1
#         else:
#             text[i]=1
#     return text
# a=input()
# print(test(a))

# def test(a):
#     if len(a)>=3:
#         res=a+"ing"
#     if "ing" in a:
#         res=a+"ly"
#     return res
# a=input()
# print(test(a))

# def test(a):
#     for i in range(1,a+1):
#         cube=i**3
#         print(f"Current Number is : {i} and the cube is {cube}")
# a=int(input())
# test(a)

# def test(a,b):
#     cnt=0
#     for i in range(len(a)-len(b)+1):
#         if a[i:i+len(b)]==b:
#             cnt+=1
#     return cnt
# a="Emma is good developer. Emma is a writer"
# result=test(a,"Emma")
# print(f"Emma appeared {result} times")

# def test(a):
#     chars = 0
#     digits = 0
#     symbols = 0
#     for char in a:
#         if char.isalpha():
#             chars += 1
#         elif char.isdigit():
#             digits += 1
#         else:
#             symbols += 1
#     return chars, digits, symbols
# str1 = "P@#yn26at^&i5ve"
# chars, digits, symbols = test(str1)
# print(f"Chars = {chars}")
# print(f"Digits = {digits}")
# print(f"Symbol = {symbols}")

# def test(a):
#     low = a.lower()
#     count = low.count("usa")
#     return count
# a = "Welcome to USA. usa awesome, isn't it?"
# result = test(a)
# print(f"The USA count is: {result}")

# def test(a):
#     words = a.split()
#     result = []
#     for i in words:
#         if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
#             result.append(i)
#     return result
# a = "Emma25 is Data scientist50 and AI Expert"
# result = test(a)
# print(result)

# def test(list1, list2):
#     difference = []
#     for i in list1:
#         if i not in list2:
#             difference.append(i)
#     return difference
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# result = test(list1, list2)
# print(result)

# def test(a):
#     cnt = list(set(a))
#     cnt.sort()
#     return cnt[-2]
# a = [10, 20, 4, 45, 99, 99]
# result = test(a)
# print(f"The second largest number is: {result}")

# def test(a):
#     for i in range(len(a)):
#         if i % 2 == 0:
#             print(a[i])
# a = "pynative"
# test(a)

# def test(a):
#     even = 0
#     odd = 0
#     for i in a:
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     print(f"Number of even numbers: {even}")
#     print(f"Number of odd numbers: {odd}")
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# test(a)