# LIST:-

    # List is a collection datatype
    # List is a heterogeneous datatype (Can store variety of data in list)
    # List is a ordered datatype
    # List supports Indexing
    # List can be created using [] or list literal.
    # List is mutable (Can be modified after creation)

#-------------------------------------------------

# How to create the list ?

# l1 = []
# print(l1)  #<class 'list'>
# print(type(l1))

# l2 = [1, 2.4, 3+5j, 'Hello', [10, 'A', 8]]
# print(l2)
# print(type(l2))


#---------------------------------------

# l3 = list()
# print(l3)
# print(type(l3))  #<class 'list'>

# l4 = list([1, -8.4, -23-4j, 'Good', 'A', [12, 'S']])
# print(l4)
# print(type(l4))


# Collection , Iterable ==> 

# ---------------------------------------------------

# Indexing on List Data type ?

    # Types of Indexing:
        # Positive Indexing ==> Left to Right, starts from 0
        # Negative Indexing ==> Right to Left, starts from -1


# list1 = [1, 2.2, 3-5j, 'Hello', [10, 20, 'A']]

# Access complete list
# print(list1)

# Access 'Hello' using +ve Index

# print(list1[3])
# print(list1[1])
# print(list1[4])


# Access 'Hello' using -ve Index
# print(list1[-2])
# print(list1[-4])
# print(list1[-1])

# ------------------------- SLICING-----------------------

# Can use +ve or -ve indexing for slicing.

# list2 = [10, 20, 30, 40, 50, 60]
# print(list2[4:1:-1])
# print(list2[-6:-1:2])
# # print a slice of list2 which is [20, 30, 40]
# print(list2[1:4:1])   # [START: END: STEP]
# print(list2[-5:-2])

# [50, 40, 30]
# print(list2[-2:-5:-1])

# [10, 30, 50]
# print(list2[0:5:2])

#-------------------- LIST BUILT IN METHODS------------------

# insertion methods:-

list3 = [1, 2]

# .append methods adds only single element at a time at right 
# list3.append(5)
# list3.append(12)
# list3.append(34)
# print(list3)

# .extend method adds multiple elements at single shot
# list3.extend([1, 23, 34, 45, 'A', [1, 2]])
# list3.extend([100, 200])
# print(list3)

# list3.insert(2, 'A')
# list3.insert(0, 100)
# print(list3)

#------------------------------------
# Remove Elements from list:

# list4 = [12, 23, 34, 45, 56, 67, 78, 89, 90, 56]

# # .remove => removes the first apperence of a specified element.
# list4.remove(56)   #[12, 23, 34, 45, 67, 78, 89, 90]
# list4.remove(12)
# # list4.remove(100) # ValueError: list.remove(x): x not in list

# print(list4)

# .pop() ==> removes element from specified index
# list4.pop(4)
# # list4.pop(15)  #IndexError: pop index out of range
# list4.pop()  # if you do not provide any index it removes the last element of list

# print(list4)

# .clear() ==> removes all elements from list and make it empty.

# list4.clear()
# print(list4)   #[]

#------------------------------------------------------

# .copy()  ==> create exact same replica of list

# l1 = [1, 2, 3, 4]

# l2 = l1

# l1.remove(4)

# print(f"l2:- {l2}, id:- {id(l2)}")
# print(f"l1:- {l1}, id:- {id(l2)}")

# l1 = [1, 2, 3, 4]

# l2 = l1.copy()

# l1.remove(4)

# print(f"l1: {l1}, id: {id(l1)}")
# print(f"l2: {l2}, id: {id(l2)}")

# l1 = [1, 2, 3, [4, 5, 6]]
# l2 = l1.copy()

# # l1.remove(3)
# l1[3][0] = 10

# print(f"l1:- {l1}, id:- {id(l1)}")
# print(f"l2:- {l2}, id:- {id(l2)}")

# import copy

# l1 = [1, 2, 3, [4, 5, 6]]

# l2 = copy.deepcopy(l1)

# l1[3][0] = 10

# print(f"l1: {l1}, id: {id(l1)}")
# print(f"l2: {l2}, id: {id(l2)}")

#-------------------------------------

# .count()

list6 = [1, 2, 1, 3, 4,2, 5, 5, 6, 1, 2, 7, 1, 1, 8, 10]

# i want the count of 1 => How many times 1 is appearing in list.

# print(list6.count(1))
# print(list6.count(5))


# Repetation

# l1 = [1, 2, 3]
# print(l1 * 2)
# print(l1 * 5)
# print(l1)


# concatination:
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(l1 + l2)

# Packing and Unpacking

# a, b, c, d, e = [1, 2, 3, 4, 5]
# print(a)
# print(b)
# print(c)
# print(d)