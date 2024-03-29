check= True
num= 49
for i in range(13,num):
    if(num%i==0):
        check=False
        
if(check==True):
     print("Prime")
else:
    print(" NOt Prime")