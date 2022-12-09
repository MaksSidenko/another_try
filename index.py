# 1

# print("go ahead")
# youtuber = "maksik"
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

# adj = input("Andjective: ")
# verb = input("Verb: ")
# madlib = f"Computer programming is so {adj}! It makes me so excited all the time \ because i love to {verb}"
# print(madlib)

# 2

# import random


# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'guess a number between 1 and {x}: '))
#         if guess > random_number:
#             print(f"No, it's bigger than this")
#         elif guess < random_number:
#             print(f"No, it's smaller than this")

#     print(f"You've guessed, this number is {random_number}")
# guess(5)

# alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
# encrypt = input("word: ")
# key = int(input("key: "))
# encrypted = ""


# pos = -1

# def listr_seatch(list, x):
#     i = 0
#     while i < len(list):
#         if list[i] == x:
#             globals()["pos"] = i
#             return True
#         i = i+1
#     return False


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = 11

# if listr_seatch(list, x):
#     print("found at", pos+1)
# else:
#     print("not found")


# pos = -1


# def listr_seatch(list, x):
#     l = 0
#     u = len(list)-1
#     while l <= u:
#         mid = (l+u)//2
#         if list[mid] == x:
#             globals()['pos'] = mid
#             return True
#         else:
#             if list[mid] < x:
#                 l = mid+1
#             else:
#                 u = mid-1
#     return False


# list = [1, 5, 7, 11, 15, 17, 27]
# x = 12

# if listr_seatch(list, x):
#     print("found at", pos+1)
# else:
#     print("not found")

# def buble_sort(list):
#     for i in range(len(list)-1, 0, -1):
#         for j in range(i):
#             if list[j] > list[j+1]:
#                 temp = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = temp


# list = [46, 4, 777, 377, 3, 854]
# buble_sort(list)

# print(list)

def selection_sort(list):
    for i in range(0, 6):
        minpos = i
        for j in range(i, 6):
            if list[j] < list[minpos]:
                minpos = j
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp


list = [10, 5, 7, 1264, 32, 35]

selection_sort(list)
print(list)
