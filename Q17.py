# Initialize a list with odd numbers and even numbers. 
# Write a function to count how many odd numbers is in a list and return the count.


l=[1,2,3,4,5,6,7,8,9]
def countodd(l):
    odd=[]
    for i in l:
        if i%2==0:
            continue
        else:
            odd.append(i)
    return len(odd)

print(countodd(l))