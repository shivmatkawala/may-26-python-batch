# File Handeling:-

    # Using File Handeling, we can create files, read files,
    # write into files, update files, append files.

# ---------------------

# File handeling has important function called "open()"

# How to create file open():

# open("sample.txt", "w")

# How to read data avaliable inside file.

# file = open("sample.txt", "r")
# content = file.read()
# print(content)

# How to write inti file

# file = open("sample.txt", "w")
# file.write("My dear comrades..!")

# How to add new content maintaining old content

# file = open("sample.txt", "a")
# file.write("\nThis is a world war..!")


# How to open file for read and write prrposes

# file = open("sample.txt", "+r")
# file.write("Indian Cinema is at top")
# print(file.read())


#----------------------

# Write

# with open("sample.txt", "w") as file:
#     file.write("India is my country..!")
#     file.close()

# with open("sample.txt", "r") as file:
#     print(file.read())
#     file.close()

# with open("sample.txt", "a") as file:
#     file.write("\nAll Indians are my friends..!")
#     file.write("\nI love my country.")
#     file.close()

# with open("sample.txt", "+r") as file:
#     content = file.read()
#     print(content)
#     file.write("\nAnd people worthy of it.")
#     file.close()


#-----------------------------

# with open("data.csv", "w") as file:
#     file.close()

