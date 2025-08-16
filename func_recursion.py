# #Functions
# # function for sum of 2 numbers
# def cal_sum(a,b):
#     s = a+b
#     return s

# a = 5
# b = 10
# print(cal_sum(a,b))
####################################
# # To print multiple lines on same line
# print("Phani", end=" ")
# print("Surya") # Even though two different print statements, result is printed on same line
#######################################
# Keeping one argument of a function always constant
# def cal_sum(a, b=2):
#     s = a + b
#     return s
# print(cal_sum(5)) # result 5 + 2 = 7
#######################################
# Printing length of a list
# cities = ["Hyd","Blore","Chen","Mum"]
# heroes = ["Thor","Ironman","Captain America"]

# def lenght_list(list):
#     return len(list)

# print(lenght_list(cities))
# print(lenght_list(heroes))
###################################
# Print elements of a list in a single line
# heroes = ["Thor","Ironman","Captain America"]

# def ele(list):
#     for val in list:
#         print(val, end=" ")
# ele(heroes)
###################################
# Factorial of n
# n = int(input("Enter number: "))
# def fact(n):
#     fact = 1
#     for i in range (1,n+1):
#         fact *= i
#     return fact
# print(fact(5))
#################################
# Convert USD into INR
# inr = int(input("Enter INR: "))

# def USDtoINR(inr):
#     usd = inr * 83
#     return usd
# print(USDtoINR(inr))
##################################
# def o_e(num):
#     if num%2==0:
#         return "EVEN"
#     else:
#         return "ODD"
# n = int(input("Enter num: "))
# print(o_e(n))
##################################
# Recursion
# Printing a series of numbers
# def show(num):
#     if(num == 0):
#         return
#     print(num)
#     show(num-1)
# show(5)
##################################
# Factorial using recursion
# def fact(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num*fact(num-1)

# print(fact(3))
#################################
# Sum of n natural numbers
# def cal_sum(n):
#     if n == 0:
#         return 0
#     return cal_sum(n-1) + n
# sum = cal_sum(3)
# print(sum)
###################################
# Print all elements of a list
heroes = ["Thor","Ironman","Captain America"]
def leng(list,index=0):
    if index == len(list):
        return
    print(list[index])
    leng(list, index+1)
leng(heroes)
