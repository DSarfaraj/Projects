#ASCII VALUE
# fro Upeer case A=65 Z=90
#for Lower case a=97 z=122
x="pYthOn"

for i in x:
    if(ord(i)>96 and ord(i)<123):  #Ordinal
        print(chr((ord(i)-32)), end= " ")
    elif(ord(i)>64 and ord(i)<91):
        print(chr((ord(i)+32)), end= " ")
    elif(ord(i)==32):
        print(i, end=" ")
