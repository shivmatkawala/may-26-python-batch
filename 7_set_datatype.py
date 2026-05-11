# Set :-
    # It is a collection datatype.
    # It doest allow to store duplicate values.
    # It is prtially heterogeneous. [value must be immutable]
    # It is unordered collection
    # It doest support Indexing
    # It is mutable (can be changed)


# Creation / Initialization of Set:-
    # {}
    # set()

# boys = {'Avi', 'sham', 'kiran', 'ravi'}
# print(boys)
# print(type(boys))


# girls = set(['rama', 'vidya', 'sonal'])
# print(girls)
# print(type(girls))

# students = set(('rajesh', 'uma', 'sandeep', 'mallesh'))
# print(students)
# print(type(students))


# fruits = set({'Mango', 'Apple', 'Grapes'})
# print(fruits)
# print(type(fruits))


# No duplicates , only uniques values
# set1 = {1, 2, 3, 4, 1, 2, 1}
# print(set1)

# hashable = Immutable = Can be changed
# unhashable = Mutable = Can be changes

# set2 = {1, 2.2, 4-8j, 'apple', [100, 200, 300]}   #TypeError: unhashable type: 'list'
# print(set2)


# set3 = {5, 4.5, 9+7j, 'Grapes', (100, 200, 300)}
# print(set3)


# set4 = {12, 23.4, 45-67j, 'Grand', {10, 20, 30}}
# print(set4)


#--------------------------------------------------

# Set doest support indexing, (No +ve, No -Ve)
# set4 = {10, 20, 30, 40}
# print(set4)

# print(set4[0])  #TypeError: 'set' object is not subscriptable


#-------------------------------------
# Membership Opertaors :- in, not in

# set5 = {10, 20, 30, 40, 50}

# print(20 in set5)  #True
# print(100 in set5)

# print(20 not in set5)
# print(100 not in set5)


# Operations on Set:

#  how to insert elements / data / values 

# set6 = set()

# set6.add(1000)
# set6.add(450.555)
# set6.add('Apple')
# set6.add(5-7j)
# # set6.add([12, 123])  #TypeError: unhashable type: 'list'
# set6.add((12, 123))

# print(set6)


# Remove element from set:
# set7 = {1, 2, 3, 4, 5}  # Removes specified elemnt
# set7.remove(100)  #KeyError: 100

# set7.remove(2)
# set7.remove(5)
# print(set7)

# set7.pop()  # Removes element randomely
# print(set7)


# Set is Mutable means set can be changed
# But inside set we can only store immutable values means only those values which can not be changed