#Loops
# While loop
# count = 1
# while count <=5 : # Prints the text untill count is not equal to 5
#     print("Hello",count)
#     count += 1 # Updation
#################################
# Print numbers from 1 to 100
# i = 1
# while i <= 100 :
#     print(i)
#     i += 1
# print("Done")
#################################
# Print numbers from 100 to 1
# i = 100
# while i >= 1 :
#     print(i)
#     i -= 1
# print("Done")
################################
# Print multiplication table of n
# num = int(input("enter number: "))
# i = 1
# while i<= 10 :
#     print(num, "*", i, "=", num*i)
#     i += 1
# print("done")
################################
# Printing values of list by loops
# lis = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i <= len(lis)-1 :
#     print(lis[i])
#     i += 1
# print("Done")
###################################
# Searching value in a tuple
# lis = (1,4,9,16,25,36,49,64,81,100)
# a = int(input("enter value: "))
# i = 0
# while i <= len(lis)-1 :
#     if(lis[i] == a):
#         print("Found at ",i)
#         break
#     i += 1
# print("Done")
####################################
# Continue statement
# i = 0
# while i <= 5:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1
# print("Done")
####################################
# for loop
# nums = [1,2,3,4,5,6]
# for val in nums:
#     print(val)
####################################
# Printing each value in list
# lis = [1,4,9,16,25,36,49,64,81,100]
# for val in lis:
#     print(val)
#####################################
# Searching number using for loop
# lis = [1,4,9,16,25,36,49,64,81,100]
# a = int(input("Enter num: "))
# i = 0
# for val in lis:
#     if val == a:
#         print("Found at: ",i)
#     i += 1
#####################################
# Range
# for i in range(10): #print 0 to 9
#     print(i)
# # range(start?,stop)
# for i in range(1,10): # print 1 to 9
#     print(i)
# # range(start?,stop,step size?)
# for i in range(1,10,2): # print all odd numbers
#     print(i)
#####################################
# Print 1 to 100
# for i in range(1,101):
#     print(i)
#####################################
# Print 100 to 1
# for i in range(100,0,-1):
#     print(i)
#####################################
# Multiplication Table
# a = 5
# for i in range(1,10):
#     print(a*i)
#####################################
# Sum of 1st n natural numbers
# n = 5
# sum = 0
# for i in range(1,n):
#     sum += i
# print(sum)
#####################################
# Factorial of a number
# n = 3
# fact = 1
# for i in range(1,n+1):
#     fact *= i
#     i += 1
# print(fact)