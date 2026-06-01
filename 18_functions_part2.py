# No Argument Functions:

# Write a function which prints fibonacci series
# upto user defined length.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 

# def generate_fibonacci_series():
#     length = int(input("How many numbers you want to generate: "))
#     num1 = 0
#     num2 = 1
#     print(num1)
#     print(num2)
#     for i in range(2, length):
#         next = num1 + num2
#         print(next)
#         num1, num2 = num2, next


# generate_fibonacci_series()


#----------------------------
# WITH ARGUMENT FUNCTIONS:

# Write a function which prints fibonacci series
# upto user defined length.

# def generate_fiboncci_series(length):
#     num1 = 0
#     num2 = 1
#     print(num1)
#     print(num2)
#     for i in range(2, length):
#         next = num1 + num2
#         print(next)
#         num1, num2 = num2, next


# generate_fiboncci_series(5)
# print("===================")
# generate_fiboncci_series(10)
# print("===================")
# generate_fiboncci_series(20)

#====================================================

# POSITIONAL ARGUMENT FUNCTIONS:

# Write a function to display product information.

# def product_info(pid, pname, supplier, category, price, region):
#     print(f"""
#             PRODUCT DETAILS:
#               Product ID: {pid}\n
#               Product Name: {pname}\n
#               Supplier: {supplier}\n
#               Category: {category}\n
#               Price: {price}\n
#               Region: {region}
#         """)
    
# product_info(101, "Coconut Oil", "Parachute", "Oil", 120, "India")
# product_info("Bread", "Italy", "Italian Bread", 102,50, "Britania" )

# KEYWORD ARGUMENT FUCTIONS

# product_info(region="America", price=200, pid=103, category="Chemicals", pname="Sunscream", supplier="Lotus")


# ==================================
# DEFAULT ARGUMENT FUNCTIONS:

# Write a program to print greet student.

# def greet(std="student"):
#     print(f"Hello Dear {std}")


# greet()
# greet("Vijay")


#-------------------------

# Write a program to print the addition of two numbers 

# def addition(num1=0,num2=0):
#     print(num1 + num2)

# addition()
# addition(5)
# addition(4, 9)


#=======================================

# VARIABLE LENGTH ARGUMENT FUNCTIONS:

# Write a function to find a maximum number 
# from provided arguments:

# def get_max(*args):
#     print(max(args))

# # get_max(3, 5)
# get_max(76, 12, 34, 90 ,100, 456, 23, 777, 190, 234)

# =================================
# Write a function to print product of numbers.
# from math import prod

# def get_product(*args):
#     print(prod(args))

# get_product(2, 3, 4, 8, 12, 9, 3)

#============================================

# VARIABLE LENGTH KEYWORD ARGUMENT FUNCTION

dict1 = {"One": 12, "Two": 20, "Three": 30, "Four": 4, "Five": 15}

# Write a program to get minimum value from given
# arguments

# def get_min(**kwargs):
#     values = kwargs.values()
#     print(min(values))


# get_min(**dict1)


#--------------------------------------

# Write a program to print consonents from provided string

# Write a program to get the number divisible by 7 from 
# entered arguments

# Write aprogram to get those values which are even
# from dict2
# dict2 = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7: 49, 8:64, 9: 81}

