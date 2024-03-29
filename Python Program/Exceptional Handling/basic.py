x="abcde"
try:
    print(4/0)
except ZeroDivisionError:
    print("Z")
except TypeError:
    print("T")
except IndexError:
    print("I")
finally:
    print("")