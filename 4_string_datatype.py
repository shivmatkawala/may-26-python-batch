# STRING DATATYPE:- 
    # String is a collection of charecters (Alphabetic, Special, Number)
    # enclosed by quotes.

    # String is an immutable Datatypes

    # String is indexed

    # String is an ordered datatype

    # String is a collection datatype

    # String is Heterogeneous


# Examples:-

    # Fruit = 'Pineapple'   # String
    # sp_char = '@#$%:}{}'  # String
    # weight = '78.5'       # String

    # Password = 'Python@#$1234'  # String

# String charecters can be enclosed by
    # 1) Single Quotes   ==>  ' '
    # 2) Double Quotes   ==>  " "
    # 3) Tripple Single Quotes  ==> '''  '''
    # 4) Tripple Double Quotes  ==> """  """

# Examples:-

todays_thought = 'A friend in "need" is friend indeed'

yesterdays_thought = "A friend in 'need' is friend indeed"


# IF STRINGS ARE VERY BIG:
tomorrows_thought = '''A friend in "need" is friend indeed.
"""Apple a Day keeps Doctors away""", Save Water, 
'''

day_after_yesterday_thought = """A friend in "need" is friend indeed.
'''Apple a Day keeps Doctors away''', Save Water, 
"""


# STRING_INDEXING:-

    # String supports 
            # +ve and -ve Indexing

#-------------------------------------

# +ve Indexing:-

name = 'Amardeep'     # length of name string ==> 8
                      # name's starting index is 0
                      # name's last index is 7

# print(name)
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# print(name[7])

# print(name[8])   #IndexError: string index out of range

# Negative Indexing

# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])
# print(name[-5])
# print(name[-6])
# print(name[-7])
# print(name[-8])


# SLICING:-  [STRAT INDEX: END INDEX: STEP]

# school = 'ST XAVIER SCHOOL'
# print(school)

# print(school[0:2:1])
# print(school[3:9:1])

# print(school[10:16:1])
# print(school[10::1])
# print(school[10::])

# print(school[-13:-7])

# # REIVAX
# print(school[-8:-14:-1])


#-----------------------------------------

# example = 'apple'

# print(example)
# print(example[3]) 
# print(example[-2])

# # app
# print(example[0:3:1])
# print(example[-5:-2:1])

string_1 = 'AWESOME'

# AEOE
# print(string_1[0:7:2])
# print(string_1[0::2])
# print(string_1[-7::2])

# EOEA
# print(string_1[-1::-2])
# print(string_1[6::-2])


#--------------------------------------------

# IN-BUILT METHODS OF STRING:-

# Method ==> Function

# Functions are building blocks to perform any 
# operations.

# In Any Prpgramming Language you find:
    # Two types of functions:
        # 1) Built In Function ==> Already ready to use, provided by programming language itself

        # 2) User-Defined Function ==> THese functions are custom and can be developed
        # by developer.


# Mobile ==> Can call, Can Text
# Fan ==> Get Cool Air

#-------------------------------------------------

# 1) Case Conversion Methods:
    # .upper()  # It converts lower case alphabetic letters to uppercase letters
    # .lower()
    # .title() # It convetrs first letter of word into upper and rest will be converted to lowercase.
    # .captalize()
    # .swapcase() # converts lower to upper and upper to lower case.

# name = 'harini reddy'
# print(name)

# print(name.upper())  #HARINI REDDY

# print(name.lower())

# print(name.title()) # Harini Reddy

# print(name.capitalize()) # Harini reddy

# state = 'TeLANgaNa'

# print(state.swapcase())  #tElanGAnA

#-----------------------------------------------------

# Search methods: These methods will give you index number of searched charecters.
    # .index()  # Index methods searches for charecter from left to right.
    # .find()
    # .rindex()
    # .rfind()

book = 'The Splendid Sun'

# index number of 'S'
# print(book.index('S'))  #4

# print(book.rindex('S')) #13

# print(book.index('Z'))  #ValueError: substring not found, Program is crashed.


# print(book.find('S'))

# print(book.rfind('S'))

# print(book.find('Z'))  # -1  ==> No programm crash


#----------------------------------

# .isalpha()
# .isdigit()
# .isalnum()

# company = 'Raybon' # all charecters are alphabetic

# print(company.isalpha())

# print(company.isdigit())

# print(company.isalnum())

# date = '12/2/2025'
# print(date.isdigit())

# weight = '45.5'
# print(weight.isdigit())

# height = '5123'
# print(height.isdigit())

# print(height.isalnum())

# password = 'Nagma@123'
# print(password.isalnum())


# .split() # it splits the string and returns list of it

string_2= 'India is my country.'

print(string_2.split())

string_3 = '12/5/2025'
print(string_3.split(sep='/'))


# strip()  # it removes left and right both the sides empty spaces

award = '    pritzker prize     '
print(award)

# lstrip()  # remove left side empty spaces
# rstrip()  # remove right side empty spaces

# print(award.lstrip())
# print(award.rstrip())
# print(award.strip())


list1 = ['Hello', 'My', 'Dear', 'Students']

# Hello My Dear Students

# string_4 = ' '
# print(string_4.join(list1).lower())


# Some other methods

# Concatination:
    # combining two or multiple strings together and forming a new string

s1 = 'thalapathy'
s2 = 'vijay'

print(s1+' '+s2)

    # Repetation

s3 = 'hari'
print(s3*2)
print(s3*5)

