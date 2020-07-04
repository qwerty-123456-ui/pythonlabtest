# Write function geometric() that takes a list of integers as input and returns True if
# the integers in the list form a geometric sequence. A sequence a0, a1, a2, a3, a4, . . . ,an is a geometric sequence if the ratios a1/a0, a2/a1, a3/a2, a4/a3, . . . , an-1/anare all equal.
# >>>geometric([2, 4, 8, 16, 32, 64, 128, 256])
# True
# >>>geometric([2, 4, 6, 8])
# False

# def geometric(l):
#     i=0
#     r=l[1]/l[0]
#     print(len(l))
#     while i<(len(l)-1):
#         rc=l[i+1]/l[i]
#         c=0
#         i+=1
#         if rc==r:
#             c=1
#             continue
#         else:
#             c=0
#             break
#     return True if c==1 else False

def geometric(iterable):
    it=iter(iterable)
    try:
        a=next(it)
        b=next(it)
        if a==0 or b==0:
            return False
        c=next(it)
        while True:
            if a*c!=b*b :
                return False
            a,b,c=b,c,next(it)
    except StopIteration:
            return True

print(geometric([2, 4, 8]))
            