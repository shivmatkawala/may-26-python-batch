# TUPLE:-
    # It is a collection datatype.
    # It is heterogeneous in nature
    # It is ordered datatype
    # It supports Indexing
    # It is Immutable in nature (Once created , cant be modified)


# Initialization / Creation Tuple:-
    # Two ways to create tuple:
        # 1) using () 
        # 2) using tuple() literal

# tup1 = ()
# print(tup1)
# print(type(tup1))  #<class 'tuple'>

# tup2 = (1, 2.2, 3-4j, 'Apple', [100, 200, 300], (1, 2, 3, 'A') )
# print(tup2)
# print(type(tup2))


# tup3 = tuple([1, 2, 'Hello', ['A', 'X', 'V']])
# print(tup3)
# print(type(tup3))


# INDEXING:-
    # Two types Indexing supported by tuple datatype:
        # +ve Indexing: starts from 0, left to right
        # -ve Indexing: starts from -1, right to left


# tup4 = (10, 20, 'A', 'B', 4.4, 5.5)

# print(tup4)

# print(tup4[2])
# print(tup4[-4])
# print(tup4[10])  #IndexError: tuple index out of range

# SLICING:-

# tup4 = (10, 20, 'A', 'B', 4.4, 5.5)
# print(tup4[1:4:1])
# print(tup4[-5:-2: 1])

# # (4.4, 'A')
# print(tup4[-2:-5:-2])
# print(tup4[4:1:-2])

#---------------------------------------------
# tup5 = (1, 2, 3, 4, 1, 2, 1,1, 15, 4, 3, 5,2)
# print(tup5.index(1))   # it returs index number of given element from left side

# print(tup5.count(1))
# print(tup5.count(2))

# packing and unpacking:

# a, b, c, d = (1, 2, 3, 4)
# print(a)
# print(b)
# print(c)

# # Concatination
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# print(t1 + t2)

# # Repetation:-
# print((12, 23, 34)*2)