# Nested if :-

citizen  = "Indian"
age = 55

if(citizen == "Indian"):
    if(age > 18 and age < 100):
        print("You r Eligible to VOTE")
    else:
        print("You r not Eligible to VOTE")
else:
    print("You r not citizen of INDIA")