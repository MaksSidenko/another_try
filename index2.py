1
# import random


# def guess(x):
#     random_num = random.randint(1, x)
#     guess_number = 0
#     while guess_number != random_num:
#         guess_number = int(input("number? "))
#         if guess_number > random_num:
#             print("less")
#         elif guess_number < random_num:
#             print("more")
#     print("done")
# guess(5)
2
# alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
# encrypt = input("your word")
# key = int(input("key"))
# encrypt = encrypt.lower()
# encrypted = ""

# for letter in encrypt:
#     pos = alphabet.find(letter)
#     newPos = key + pos
#     if letter in alphabet:
#         encrypted = encrypted + alphabet[newPos]
#     else:
#         encrypted = encrypted + letter

# print(encrypted)

3

# pos = -1


# def linear_search(x, list):
#     i = 0
#     while i < len(list):
#         if x == list[i]:
#             globals()['pos'] = i
#             return True
#         i = i+1
#     return False


# x = 66
# list = [1, 5, 7, 66, 3, 4, 5]

# if linear_search(x, list):
#     print("found at", pos+1)
# else:
#     print("not found")
