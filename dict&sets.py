# #Dictonaries
# #Store data values in key:value pairs, unordered, mutable, no duplicate keys
# info = {
#     "name" : "Surya",
#     "age" : 20,
#     "subjects" : ["Java","C"],
#     12 : 91.1
# }
# # print(type(info))   Type checking 
# # print(info["name"]) printing elements
# # print(info["age"])
# # info["age"] = 21     Accessing individual elememt
# # print(info)
# info["hero"] = "Tony"  #Adding new element
# print(info)
##############################################
# #creating new dictionary
# null_dict = {}
# null_dict["name"] = "Tony Stark"
# print(null_dict)
##############################################
# #Nested Dictionary
# student = {
#     "name" : "Surya",
#     "subjects" : {
#             "phy" : 100,
#             "chem" : 99,
#             "math" : 200,
#     },
#     "roll" : 472
# }
# print(student["name"])
# print(student["subjects"]["chem"])
##############################################
#Dictonary methods
# student = {
#      "name" : "Surya",
#      "subjects" : {
#              "phy" : 100,
#              "chem" : 99,
#              "math" : 200,
#      },
#      "roll" : 472
# }
# print(student.keys()) #Nested dict not printed
# print((student.values())) # Prints all values
# pairs = list((student.items())) #Pair of key and val printed
# print(pairs[0])
# print(student.get("name")) # Returns value of a key
# student.update({"city" : "Hyd"}) #Updating dictionary
# print(student)
###########################################
#sets
# Collection of unordered items
# Unique and set is mutable but values are immutable
# collection = {1,2,"Surya",3.99,1}
# print(type(collection))
# print(collection) # Duplicate values ignored
# print(len(collection)) # Duplicate values are not included
# emp_set = set{} # Empty set declaration syntax
################################################
# collection = set()
# collection.add(1) #adding elements
# collection.add("a")
# collection.add(5)
# collection.add((1,2,4)) #adding tuple
# #collection.add([3,4,5]) #adding list -> Error
# collection.add(10)
# collection.remove(10) #removing elements
# print(collection)
# collection.clear() # empties the complete set
# print(len(collection))
# surya = {"S","u","r","y","a"}
# print(surya.pop()) #random elements are popped and returned
# print(collection.union(surya)) # Union of 2 sets
# print(collection.intersection(surya)) # intersection of 2 sets
############################################
# To store 2 or more values for a key, we can use list or tuple
# dictionary = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture","list of facts"]
# }
# print(dictionary)
############################################
# Reading and adding values into dictonaries
subjects = {}

subjects.update({"sub1" : input("enter sub1 marks: ")})
subjects.update({"sub2" : input("enter sub1: ")})
subjects.update({"sub3" : input("enter sub1: ")})
print(subjects)
##############################################
