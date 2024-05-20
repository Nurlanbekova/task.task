
# Задания2
# N = int(input())
# arr = []
# res = 1
# for i in range(1, N + 1):
#     res *= 2
#     arr.append(res)
# print(arr)



# Задания3
# N = int(input('...'))
# A = int(input('...'))
# D = int(input('...'))
# arr = []
# for i in range(N):
#     arr.append(A + i * D)
# print(arr)

# задания4

# N = int(input('...'))
# A = int(input('...'))
# D = int(input('...'))
# arr = []
# for i in range(N):
#     x = A * (D**i)
#     arr.append(x)
# print(arr)
#

#array5
# #
# F = [0, 1]
# N = 20
# for i in range(2, N):
#     num = F[i - 2] + F[i - 1]
#     F.append(num)
# print(F)


#array6

# N = 10
# A = 1
# B = 2
# arr = [A,B]
# for i in range(2, N):
#     num = sum(arr)
#     arr.append(num)
# print(arr)
#
#
# #array7
#
# N = 10
# arr = []
# for i in range(N):
#     num = N - i
#     arr.append(num)
# print(arr)

#
#
#
# задания 8
# array = [1,2,4,5,6,2,3,645,324]
# k = []
# for i in array[::-1]:
#     if i % 2 != 0:
#         k.append(i)
#
# print(k)
# #
# # Задания 9

# array = [3,645,324,88]
# k = []
# for i in array[::-1]:
#     if i % 2 == 0:
#         k.append(i)
#
# print(k)

#
# # Задания 10
#
# array=[3,48,892,36,23,45,32]
# chot=[]
# nechot=[]
# for i in array:
#     if i %2==0:
#         chot.append(i)
#d
# for i in array[::-1]:
#     if i % 2 !=0:
#         nechot.append(i)
#
# print(chot)



# print(nechot)






# k = {'kazaknews': 'Казакстан', 'year': 2024, 'id': 1}
# d = {'kazaknews': 'Бишимбаев', 'year': 2023, 'id': 2}
# l = {'ala_kachuu_news': 'Ала качуу 2024', 'year': 2021, 'id': 3}
#
#
#
# news = [{'kazaknews': 'Казакстан', 'year': 2024, 'id': 1},
#         {'kazaknews': 'Бишимбаев', 'year': 2023, 'id': 2},
#         {'ala_kachuu_news': 'Ала качуу 2024', 'year': 2021, 'id': 3},]
#
# search=input("Введите год:")
#
# search_news = []
# for index in range(len(news)):
#     if search in news[index]['title']:
#         search_news.append(news[index])
#
#
#
# archives = []
#
#
# t = [k, d, l]
# for item in t:
#     if item['year'] == 2021:
#         print('Новости 2024')
#
# for item in news:
#     if item['year'] != 2024:
#         archives.append(item)
#
#
#
# print('Архив:')
# for archived_item in archives:
#     print(archived_item)
#
#




