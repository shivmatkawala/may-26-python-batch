# Control Statements (LOOPS):-
    # Types of Loops:-
        # 1)while loop
            # More Manual
            # more control

        # 2) for loop
            # more automatic
            # less control
        

# Exmaple:-

# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")


#---------------- WHILE LOOP-----------------

# count = 0

# while count < 20:
#     print("Hello World")
#     count +=1


#-------------------------

# print 1 to 10 all the numbers using while loop 

# number = 1

# while number <= 10:
#     print(number)
#     number +=1


#-----------------------------
# write a program to print all the even numbers from 15 to 50
# using while loop.

# number = 15

# while number < 50:
#     if number % 2 == 0:
#         print(number)
#     number += 1


# Write a program to print all odd numbers from 100 to 80
# using while loop

# number = 100

# while number > 80:
#     if number % 2 != 0:
#         print(number)
#     number -= 1


# Write a program to print all the numbers which are divisible by
# 5 in between 50 and 100 using while loop

# number = 50

# while number < 100:
#     if number % 5 == 0:
#         print(number)
#     number +=1

#-------------------------

# ask user to provide his / her name using input function 
# check if there are any vowels and print them using while loop
# shivkumar
# name = input("Enter your name: ")
# index = 0
# print(len(name))
# while index < len(name):
#     if name[index] in "aeiouAEIOU":
#         print(name[index])
#     index +=1


# -----------------------------------

# Write a program to print fibonacci series upto 20 numbers

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
# num_of_nums = int(input("How many fibonacci numbers you want: "))

# num1 = 0
# num2 = 1
# print(num1)
# print(num2)
# count = 0

# while count < num_of_nums-2:
#     new = num1 + num2
#     print(new)
#     num1 = num2
#     num2 = new
#     count +=1


#-------------------------

# write a program to print  all the numbers which are 
# divisible by 5 and 3 in between 0 and 100

# count = 0

# while count < 100:
#     if count % 5 == 0 and count % 3 == 0:
#         print(count)
#     count +=1


#----------------------

list1 = [1, 2.2, "A", 67, "Hello", 7-5j, [1, 2, 3], "B"]

# from list1 print only strings using while loop.

index = 0

# while index < len(list1):
#     if type(list1[index]) == str:
#         print(list1[index])
#     index +=1

# while index < len(list1):
#     if isinstance(list1[index], str):
#         print(list1[index])
#     index +=1

#--------------------------

#------ for loop:-

# Write a program to print "Hello World" 5 times.

# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

# count = 0

# while count < 5:
#     print("Hello World")
#     count+=1

# for count in range(0, 5):
#     print("Hello World")


#----------------------
# Write a program to print tabale of 9

# for count in range(1, 11):
#     print(f"9 * {count} = {9*count}")


#--------------------
# Write a program to print all odd numbers 
# from 50 to 70 

# for num in range(50, 71):
#     if num % 2 != 0:
#         print(num)
#     else:
#         pass

#----------------------------
# Write a program to print all numbers from a str1
# str1 = "Ah4&*io)012'"
# # print(len(str1))
# for index in range(0, len(str1)):
#     if str1[index].isdigit():
#         print(str1[index])
        

# Write a program to print all numbers divisible by 7 
# from list1

list1 = [45, 12, 14, 56, 81, 90, 77, 84]

# for num in list1:
#     if num % 7 == 0:
#         print(num)


# for index in range(0, len(list1)):
#     if list1[index] % 7 == 0:
#         print(list1[index])


#--------------------
# Write a program to print user specified number of 
# fibonacci series.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233


# num_of_nums = int(input("How many numbers of fibonacci series you want: "))
# num1 = 0
# num2 = 1
# print(num1)
# print(num2)

# for i in range(2, num_of_nums):
#     new = num1 + num2
#     print(new)
#     num1, num2 = num2, new


# -----------------------------

# print even and divisble by 4 numbers in between 90 to 70.


# for num in range(90, 70, -1):
#     if num % 4 == 0:
#         print(num)


#------------------

# Write a program to print all armstrong numbers in between 
# 100 and 10000

# 153 ==> (1** 3) + (5**3) + (3**3)
#     ==> 1 + 125 + 27
#     ==> 153

#-------------------------

# for num in range(100, 10000):
#     power = len(str(num))
#     total = 0
#     for digit in str(num):
#         total += (int(digit) ** power)
#     if total == num:
#         print(num)

#------------------------------
