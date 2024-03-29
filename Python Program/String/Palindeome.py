# y = "sitin" 
# x=y[::-1]
# if(x==y):
#     print("Palindrome")
# else:
#     print("NOt Palindrome")

x = "python"
y = " "
last= len(x)-1
middle= len(x)//2

for i in range(last,-1,-1):
    y+= x[i]
    if(x==y):
        print("P")
    else:
        print("NP")
print(y)

#ASCII VALUE
# fro Upeer case A=65 Z=90
#for Lower case a=97 z=122