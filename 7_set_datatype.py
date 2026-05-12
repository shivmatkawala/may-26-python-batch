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

#-----------------------------------------------------------------

# SET Operations:-

# Union    |
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# set3 = set1 | set2
# print(set3)    #{1, 2, 3, 4, 5, 6}


# Difference    -
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# set3 = set1 - set2
# print(set3)    #{1, 2}

# set4 = set2 - set1
# print(set4)    #{5, 6}

# Intersection   &
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}


# set3 = set1 & set2     
# print(set3)   #{3, 4}


#--------------------------------

# set1 = {10, 34, 45, 67, 9}
# set2 = {34, 45, 45, 67, 1}

# Union 

# set3 = set1.union(set2)
# print(set3)

# Difference
# set4 = set1.difference(set2)
# print(set4)

# set5 = set2.difference(set1)
# print(set5)


# Intersection

# set6 = set1.intersection(set2)
# print(set6)

#------------------------------------

# Symmetric Difference:-

set1 = {"A", "B", "C", "D"}
set2 = {'C', 'D', "E", "F"}

# set3 = set1.symmetric_difference(set2)
# print(set3)

# Symetric Difference Update:-
# set1.symmetric_difference_update(set2)
# print(set1)

# set2.symmetric_difference_update(set1)
# print(set2)

# Intersection Update
# set1.intersection_update(set2)
# print(set1)

# set2.intersection_update(set1)
# print(set2)

# Difference Update
# set1.difference_update(set2)
# print(set1)

# set2.difference_update(set1)
# print(set2)


#----------------------------------------

# set1 = {1, 2, 3, 4, 5, 6}  # superset of set2
# set2 = {4, 5}  # subset  of set1

# print(set1.issuperset(set2))  #True
# print(set2.issubset(set1))  # True

# print(set1.issubset(set2))
# print(set2.issuperset(set1))


# s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9 ,0 , -1}
# s2 = {True, 2, 3, False}

# print(s1.issuperset(s2))  #True
# print(s2.issubset(s1))


#----------------------------
# disjoint

# s1 = {4, 5, 6, 7, 8}
# s2 = {7, 8, 9, 10, 11}
# print(s1.isdisjoint(s2))  # False



# Repetation cant be performed on set

# Packing & Unpacking
# a, b, c = {10, 2, 3}
# print(a)
# print(b)
# print(c)

# Concatination is not possible on set
