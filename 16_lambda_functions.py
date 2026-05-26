# Lambda Functions:-    
    # Anonymous / nameless functions
    # lambda is single line program
    # we can store lambda as a value in variable
    # lambda functions are good to use for simple and easy logics
    # lambda functions are easy to read, maintain
    # lambda functions are faster than normal functions.
    # Reusibilty of code increases.

# How to create a lambda function.

# square = lambda num: num ** 2

# print(square(5))
# print(square(9))

#-------Practice:

# Write a lambda function to double the number.
# double = lambda num: num + num
# print(double(6))
# print(double(149))


# Write a lmbda function to repeat the string
# repeat = lambda string: string * 2
# print(repeat("Hello"))

# Write a program to print wheter the number is even or odd.
# even_or_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
# print(even_or_odd(7))
# print(even_or_odd(18))

# Write a lmabda function to make a string capital case.
# apple ==> APPLE
# capital = lambda string: string.upper()
# print(capital("apple"))
# print(capital("minister"))

# Write a lambda function to reverse list.
# reverse = lambda list: list[::-1]
# print(reverse([1, 2, 3, 4]))


# write a lambda function to get the vowels from string and print them.
# string1 = "amanora"

# vowels =  list(filter(lambda char: char if char.lower() in "aeiou" else "", string1))
# print(vowels)

#---------------------------------
# write a lambda function to get the special charecters from
# list1

# list1 = ["A", "%", "1", "i", "*", "V"]

# special_chars = list(filter(lambda char: char if not char.isalnum() else "", list1))
# print(special_chars)

# -------------------------

# Write a lambda function to get the sum of all numbers
# from list2
# list2 = ["e", "H", "^", 1, "7", 9, True]
# list2 = [1, 2, 3, 4, 5]

# from functools import reduce

# addition = reduce(lambda num1, num2: num1 + num2, list2)
# print(addition)

# numbers = list(filter(lambda element: element if type(element) == int else "", list2))
# print(numbers)

# addition = reduce(lambda num1, num2: num1+ num2, list(filter(lambda element: element if type(element) == int else "", list2)))
# print(addition)

#-------------------------------------------

# write a lambda function to get the product of all floats 
# from tup1

from functools import reduce


# tup1 = ("&", 5, 7.9, 2.3, "J", 5+8j, 0.5)

# product_of_floats = reduce(lambda f1, f2: f1 * f2, list(filter(lambda num: num if type(num) == float else "", tup1)))
# print(product_of_floats)

#-------------------------------

# l1 = [3, 4, 5, 6, 7, 8, 9]

# results = list(map(lambda num: num** 2, l1))
# print(results)


# lower the letters using map and lambda

# str1 = "HAKUNAMATATA"

# result = "".join(list(map(lambda x: x.lower(), str1)))
# print(result)


#---------------------------------------
# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# t1 = (1, 2, 3, 4, 5, 6, 7, 8)
# s1 = {1, 2, 3, 4, 5, 6, 7, 8}
# str1 = "HellO"
# d1 = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64}

# # map   ==> to perform operation on each element of collection
# l2 = list(map(lambda num: num * 2, l1))
# print(f"l2: {l2}")

# # filter => to filter out the collection 
# l3 = list(filter(lambda num: num if num%2 ==0 else "", l1))

# print(f"l3: {l3}")
# # reduce => to get simgle element as aanswer
# l4 = reduce(lambda num1, num2: num1 + num2, l1)
# print(f"l4: {l4}")
