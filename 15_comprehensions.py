# Comprehensions:-


# list1 = [2, 4, 6, 8, 10]

# evans = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         evans.append(i)
# print(evans)

# List Comprehension:

# evens = [num for num in range(1, 11) if num % 2 == 0]
# print(evens)

#--------------------------------

# write a list comprehension to get all numbers in between 20 to 50
# divisible by 3

# divisible_by_3 = [num for num in range(20, 50) if num % 3 == 0]
# print(divisible_by_3)

# Write a list comprehension to get the consonents from
# str1 string.

# str1 = "782FDGimaO"

# consonents = [char for char in str1 if char.isalpha() and char not in "AEIOUaeiou"]
# print(consonents)

#--------------------------------

# Write a list comprehension to get the all 
# odd numbers in between 100 and 10 which are
# divisible by 3 and 7

# odds = [num for num in range(100, 10, -1) if num % 2 != 0 and num % 3 == 0 and num % 7 == 0]
# print(odds)


# write a list comprehension which contains day, month, and year
#ask user to provide dob(mm/dd/yyyy) you print 
# dob = input("enter dob: ")

# list1 = [int(value) for value in dob.split("/")]
# print(list1)


# -------------------------
# Tuple Comprehension:-

# use tuple comprehension and create a table of 19

# table_of_19 = (num*19 for num in range(1, 11))

# print(table_of_19)  #<generator object <genexpr> at 0x0000020DAE909490>

# for i in table_of_19:
#     print(i)


#------------------------------
# Set comprehension: 

# set1 = {num for num in range(1, 100) if num % 5 == 0}
# print(set1)


# Dictionary comprehension:

# write a dict comoprehehsnion to get number as 
# a key and its square as a value in between 1 and 10

# dict1 = {key:key**2 for key in range(1, 11)}
# print(dict1)

# create a dictionary comprehnsion of all charecters from str1
# as a key and its ascii code as Value
# str1 = "hello@123"
# dict2 = {key:ord(key) for key in str1}
# print(dict2)

