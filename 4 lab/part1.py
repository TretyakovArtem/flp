#1.1
# list_of_num = [23, 5, 43, 17]
# sum = 0
# for num in list_of_num:
#     sum += num
# avg = sum / len(list_of_num)
# print(avg)



#1.2
# s = "Съешь еще этих мягких французских булок, да выпей чаю"
# print(s[:9] + s[49:])


#1.3
# values = [4, 6, 8, 16, 44]

# values.pop()
# values.remove(4)

# print(values)

#1.4
# list_of_num = [23, 5, 43, 17]
# sum = 0
# for num in list_of_num:
#     sum += num
# avg = sum / len(list_of_num)
# print(avg)

#1.5 (1)
# result = []
# temp = 2
# for num in range(9):
#     result.append(temp)
#     temp += 2

# print(result)

# 1.5 (2)
# result = []
# temp = 50
# for num in range(11):
#     result.append(temp)
#     temp -= 10

# print(result)

#1.6

# fruits = ['apple', 'orange', 'pear', 'banana']

# def not_unique(l):
#     passed = []
#     for element in l:
#         for p in passed:
#             if p == element:
#                 return "List contains not uinique values"
#         passed.append(element)

# print(not_unique(fruits))

#1.7

# a = ['name', 'age', 'favorite_movie']
# b = ['ivan', '20', 'titanik']

# result = {}

# for f, v in zip(a, b):
#     result[f] = v

# print(result)