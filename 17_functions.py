# Functional Programming Paradigm:
    # It is just way of writing a code
    # It allows to execute the code only when needed
    # you can call the function multiple times and excecute mu;ltiple times
    # functions do increase the reusibility of code.



# Write a program to get all even numbers from 20 to 50
# def evens():
#     for i in range(20, 50):
#         if i % 2 == 0:
#             print(i)

# Write a program to print "Hello World"
# def greet():
#     print("Hello World")

# Write aprogram to reverse a list
# def reverse_list():
#     l1 = [1, 2, 3, 4, 5, 6, 7]
#     print(l1[::-1])


# reverse_list()


# greet()
# greet()
# greet()
# greet()

# reverse_list()


#-----------------------------------

# Functions are created in two parts:
    # 1) head of the functions
    # 2) body of the functions

# def funtion_name():     # head of the fucntions
    # code              # body of the functions


#------------------------------------
    # Types of of functions:
        # 1) no argument functions
            # if the function has no argument then that is no argument function
        
        # 2) with argument functions
                # 1) positional argument function
                # 2) default argument function
                # 3) keyword argument function
                # 4) variable length arguments function
                # 5) variable length keyword arguments function

#--- No ARGUMENT
# def greet():
#     print("Hello Friend..")

# greet()


# WITH ARGUMENT
# def greet(name):
#     print(f"Hello {name}")

# greet("Pramila")
# greet("Laxmi")
# greet("Shravya")


# POSITIONAL ARGUMENT

# def my_info(name, age, gender):
#     print(f"My Name is {name}\nMy Age is {age}\nI am {gender}")

# my_info("Sachin", 20, "Male")
# my_info("Male", "Sachin", 20)


# DEAULT ARGUMENT

# def greet(name="Buddy"):
#     print(f"Hello {name}")

# greet()
# greet("Pramila")

# KEYWORD ARGUMENT

# def my_info(name, age, gender):
#     print(f"My name is {name}\nMy Age is {age}\nMy Gender is {gender}")

# # my_info("Female", "Gauthami", "23")
# my_info(gender="Female", name="Gauthami", age=23)

#----------------------------
# variable length arguments

# def employee_detail(eid, firstaname, lastname, email, salary):
#     print(f"My Details: \nEID: {eid}\nFIRSTANAME: {firstaname}\nLATNAME: {lastname}\nEMAIL: {email}\nSALARY: {salary}")

# employee_detail(101, "Rakesh", "Dholkia", 'rk@gmail.com',45000)


# def addition(*args):
#     print(sum(args))

# addition(2, 4, 7, 5,20, 5, 34, 89)

# addition(2, 3)


# VARIABLE LENGTH KEYWORD ARGUMENTS

# dict1 = {'1':1, '2':4, '3':9, '4': 16, '5':25}

# def xyz(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)


# # xyz(one=1, two=4, three= 9, four=16, five=25)
# xyz(**dict1)

