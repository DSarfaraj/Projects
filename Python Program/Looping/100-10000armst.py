for num in range(100,10000):
     t1 = num
    digit = 0

    while(t1>0):
        t1//10
        digit+=1

    t2 = num
    sum = 0
    while(t2>0):
        rem = t2%10
        multi = rem**digit
        sum+=multi
        t2//=10
    if(sum == num):
        print(sum)