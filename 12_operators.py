# Operators:-

    # Arithmetic Operators
        # Addition +
# num1 = 4
# num2 = 6
# print(num1 + num2)

#         # Substraction -
# print(num1 - num2)

#         # Multiplication *
# print(num1 * num2)

#         # True Division  /
# num3 = 5
# num4 = 3
# print(num3 / num4)

#         # Floor Division //
# print(num3 // num4)
# print(17 // 5)

#         # Exponentiation (Power)  **
# print(num1 ** num2)

#         # Modulus (mod)  %
# print(17 % 5)


#-------------------- Comparision Operators:

# x = 5
# y = 3

# # Greater than >
# print(x > y)

# # Lesser than <
# print(x < y)

# # Greater than or equal to >=
# print(x >= y)

# # Lesser than or equal to <=
# print(x <= y)

# # equal to ==
# print(x == y)

# # not equal to !=
# print(x != y)


# ------------------- Assignment Operators
# x = 5

    # assign operator =
    # Add and assign +=
# x+=2
# print(x)

    # Substract and assign -=
# x-=3
# print(x)

    # Multiply and assign *=
# x*=4
# print(x)

    # true divide and assign  /=
# x/=2
# print(x)
    # floor divide and assign //=
# x //=3
# print(x)

    # mod and assign %=
# x%=3
# print(x)

    # exponent and assign **=
# x **= 4
# print(x)

#======================================

# num1 = 55
# num1 = num1 + 5
# num1+=5
#--------------------------------------

# Identity Operators:
    # is
    # is not

# x = 5
# y = 5

# print(x is y)

# print(id(x))
# print(id(y))
# import copy

# z = [10, 20]
# m = copy.deepcopy(z)
# print(z, id(z))
# print(m, id(m))

# print(z is m)
# h = 10
# s = h
# print(id(h))
# print(id(s))

# print(h is not s)

#-----------------------------
# Membership operators:
    # in 
    # not in

# s1 = {12, True, "Hello", "B", 5.5}
# print(1 in s1)
# print(12 not in s1)
# print("hello" is s1)

#-------------------------

# bitwise operators:-

# print(5 & 2)

# print(bin(2))

# print(int('00000000', 2))

# OR
# print(5 | 2)

# print(int('111', 2))


# XOR

# print(11 ^ 7)

# print(bin(11))
# print(bin(7))
# print(bin(12))



# --------------------Logical Operators:

# and

x = 5
y = 10
z = 15

# print(x is y and y is not z)
# False and True  ==> False

# print(x < y and y < z and z > x)
# True and True and True ==> True

# print(x != y and y != z)
# True and True  ==> True

# ---------------------------

# or
# print(x is not y or y is z)
# True or False  ==> True

# print(z > y or y > x)
# True or True ==> True

# print(z < y or y < x)
# False or False ==> False

# not

# print(not(x > y))

# print(not(z is y))

# print(not(x <= y))



# ----------------------- Ternary Operator:

fav_primary_color = input("Enter your favourate Primary color: ")

# print(fav_primary_color)

# Green ===> Nature
# Red ==> Sacrifice
# Blue ==> Peace

# result = "Nature" if fav_primary_color == 'Green' else "Sacrifice" if fav_primary_color == "Red" else "Peace" if fav_primary_color == "Blue" else "Invalid Color."

# print(result)


# Write a program where you ask user to enter
# age. 
# if user age is bellow 18  print "Minor"
# if user age is 18 or bellow 50 "Major"
# id user age  is above 50 "Old"
