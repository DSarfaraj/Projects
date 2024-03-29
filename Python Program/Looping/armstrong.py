num = 153
t1 = num
digit = 0
while(t1>0):
    t1//10
    digit+=1

#find product
t2 = num
sum = 0
while(t2>0):
    rem = t2%10
    multi = 1
    for i in range(1,digit+1):
        multi*=rem
    
    #sum
    sum+=multi
    t2//=10

#compare
if(sum==num):
    print("Armstron")
else:
    ("Not Armstrong")
