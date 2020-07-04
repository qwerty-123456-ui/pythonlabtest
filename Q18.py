# Implement function names() that takes no input and repeatedly asks the user to enter the first name of a student in a class. When the user enters the empty string, the function should print for every name the number of students with that name.
# >>>names()
# Enter next name: Valerie
# Enter next name: Bob
# Enter next name: Valerie
# Enter next name: Amelia
# Enter next name: Bob
# Enter next name:
# There is 1 student named Amelia
# There are 2 students named Bob
# There are 2 students named Valerie


def names():
    a = True
    n=[]
    while a:
        s=input("Enter next name : ")
        if s!='':
            n.append(s)
        else:
            break
    l={}
    for i in n:
        if i not in l:
            l[i]=n.count(i)
            # print(f"There are {n.count(i)} student named {i}")
    # print(l)
    for i in sorted(l.keys()):
        print(f"There are {l[i]} student named {i}")
names()
