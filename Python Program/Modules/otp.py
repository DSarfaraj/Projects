# import random as r  #as-Alias
# file=open("C:\\Users\\sarfa\\Desktop\\Python Program\\Modules\\otp.txt")

# "Want to Login?"

# login = input("Want to login: ")

# if(login == "Y"):
#     otp= r.randint(1000,9999)

#     try:
#         print(file.tell())
#         file.writelines(str(otp))
#         print(file.tell())
#     except(FileExistsError):
#         print("")
#     except(FileNotFoundError):
#         print("")

#     print("otp is",otp)
#     f_otp= int(input("Enter otp u hve receive"))
#     if(otp==f_otp):
#         print("user login successfull")
#     else:
#         print("Incorrect otp")
# else:
#     print("f9")

import random as r #alias
file = open("C:\\Users\\sarfa\\Desktop\\Python Program\\Modules\\otp.txt", "w")
def Login():

    # 1) Login
    login = input("Press Y to login!!")

    if(login=="Y"):
        otp = r.randint(1000,9999)
        
        try:
            file.writelines(str(otp))
            
        except(FileNotFoundError):
            print("File doesn't exist")
        except(FileExistsError):
            print("Cannot create file , already exists!!")
        
        file.close()

        print("Your OTP has been sent!!")
        f_otp = int(input("Enter the OTP you have recieved : "))
        if(otp==f_otp):
            print("User Login Successfull")
        else:
            print("OTP Incorrect")
    else:
        file.close()
        print("See you soon!!!")
        repeat = input(" Do u Want ti try again? Y/N")
        if(repeat=="Y"):
            print("")

Login()