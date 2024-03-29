count= 0
sum= 0
# find prime no. b/w 13 to 49 then count & sum of them.
for i in range(13,49):
    num1= i
    check= True

    for i in range(2, num1):
         if(num1%i==0):
            check=False

    if(check==True):
        count+=1
        sum+=num1
        
print(count)
print(sum)