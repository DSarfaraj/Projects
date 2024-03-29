# if - elif - else
# nested if

marks = 565

if(marks>80 and marks<=100):
    print("A Grade")
elif(marks>65 and marks<=80):
    print("B Grade")
elif(marks>45 and marks<=65):
    print("C Grade")
elif(marks>33 and marks<=45):
    print("D Grade")
elif(marks>0 and marks<=33):
    print("FAIL")
else:
    print("Invalid MArks")