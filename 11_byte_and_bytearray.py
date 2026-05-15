# byte :-
    # bytes are nothing but a charecters representation in memory

# ASCII CODE :-

# A => 65
# B => 66
# C ==> 67

# Formula to fnd a a ascii code of charecter

# print(ord("A"))  # 65
# print(ord('a'))  # 97
# print(ord("%"))  # 37


# print(bin(65))  #1000001

# print(int('1000001', 2))  #65

# print(chr(65))  # A

#---------------------------------

# b1 = bytes("A",encoding="utf-8")
# print(b1)
# print(type(b1))

# b2 = b"Apple"
# print(b2)
# print(type(b2))


#----------------------

# b3 = b"ABCDE"
# print(b3[0])
# print(b3[1])
# print(b3[3])

#------------------- Bytearray

# b_ar1 = bytearray([97,98, 99, 100, 101])
# print(b_ar1)   #bytearray(b'abcde')
# print(type(b_ar1))

# b_ar2 = bytearray([67, 34, 104, 55])
# print(b_ar2[0])
