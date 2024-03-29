## Create Function

# def is_even(x):
#     if(x%2==0):
#         return "Even"
#     else:
#         return "Odd"
    
# print(is_even(x))

## Using Lambda 

# is_even = lambda x:"Even" if x%2==0 else "Odd"   #lambda = Annonimous (no name & directly store in a variable, one time use, single line )
# print(is_even(5))

# is_even = lambda a,b,c:a+b+c
# print(is_even(2,5,8))

#fillter
#map
#reduce


# def checkeven(x):
#     if(x%2==0):
#         return "Even"
#     else:
#         return "Odd"
# num = [0,1,2,3,4,5,6,7,8,9]
# even= filter(checkeven(x),num)


# # Division = Dividend / Divisor = Quotient
# divisor= lambda x:x
# def divide(divident):
#     return divident/divisor(11)
# print(divide(10))



# def loud(func):
#     return func.upper()
# def quiet(func):
#     return func.lower()
# talk = lambda words:words
# print(loud(talk("I m listening")))


##filter fuct = fetch value which satisfy function
# num = [0,1,2,3,4,5,6,7,8,9]
# even_num = list(filter(lambda x:x%2==0, num))
# # print(type(even_num))
# print(even_num)
# # for i in even_num:



##map funct
from functools import reduce

num = [0,1,2,3,4,5,6,7,8,9]
even_num = list(filter(lambda x:x%2==0, num))

newl = list(map(lambda x:x+10, even_num))
print(newl)

sum_of_list= reduce(lambda a,b:a+b, newl)
print(sum_of_list)

# print(type(sum_of_list))