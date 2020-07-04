# Given a list of integers, combine all integers to form a single integer.
# Eg:  [1,25,32,4,5] ==> 1253245

def single(l):
    s=''
    for i in l:
        s+=str(i) 
    return s

    
print(single([1,25,32,4,5]))