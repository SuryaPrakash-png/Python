# File IO
# Python can be used to perform operations on a file
# Text Files: .txt,.docx,.log,...
# Binary Files: .mp4,.mov,.png,.jpeg,...
#############################################
# Open a file f = open("file_name","mode") mode = r,w Default: read
# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()
#############################################
# Read only specific number of characters
# f = open("demo.txt","r")
# data1 = f.read(6)
# print(data1)
# f.close()
###############################################
# Read only one line at a time
# f = open("demo.txt","r")
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# f.close()
##############################################
# Writing to a file
# Write mode w: Clears all existing data and writes new data
# f = open("demo.txt","w")
# f.write("I am Loki the King of Asgard")
# f.close()
# Append mode "a": Adds the text to existing data
# f = open("demo.txt","a")
# f.write("\nI am Surya and I love you 3000")
# f.close()
################################################
# Create a file
# f = open("sample.txt","w")
# f.close() # File gets automatically created 
##################################################
# Read and write(Overwrite) modes at the same time "r+" Overwrites the file from the starting point
# "w+" 1st erase out all the data in the existing file and then write the new data
# "a+" Read and append mode
##################################################
# "with" syntax
# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)
# with open("demo.txt","w") as f:
#     f.write("New data")
###################################################
# Deleting a file (using os module)
# import os
# os.remove("sample.txt") # Deletes the file permanently
####################################################
# Creating a new file and adding data into it
# f = open("practice.txt","w")
# f.close()
# d = open("practice.txt","w")
# d.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java.")
# d.close()
####################################################
# Replacing "Java" by "Python" in the file
# with open("practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("Java","Python")

# with open("practice.txt","w") as f:
#     f.write(new_data)
####################################################
# To search if "learning" wrod is present in the file
# def check_word():
#     word = "learning"
#     with open("practice.txt") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not Found")
# check_word()
####################################################
# To find in which line "learning appears 1st"
# def check_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_line()
#########################################3
# Finding even numbers in a file containing numbers separated by ','
count = 0
with open("practice.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count += 1
print(count)  
