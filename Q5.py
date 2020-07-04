# 5.Write an interactive python program having a function called Initials() that takes input  representing a full name and returns the initials of the name in all capital letters. For example If Input: Robert B. Qwerty   then Output : RBQ

def Initials(n):
    s=''
    for i in n.split():
        s+=i[0]

    return s.upper()

name=input("Enter your name : ")
print("Initials are :  "+ Initials(name))