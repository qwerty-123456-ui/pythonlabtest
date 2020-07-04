# Let list1 and list2 be two lists of integers.We say that list1 is a sublist of list2
# if the elements in list1 appear in list2 in the same order as they appear in list1, but not necessarily consecutively.
# >>>sublist([15, 1, 100], [20, 15, 30, 50, 1, 100])
# True
# >>>sublist([15, 50, 20], [20, 15, 30, 50, 1, 100])
# False


l1=[15,20,100]
l2=[20,15,30,50,1,100]

# def sublist(l1,l2):
#     c=[]
#     for i in l1:
#         if i in l2:
#             c.append(l2.index(i))
#     l=[]
#     for i in c:
#         l.append(i)
#     c.sort()
#     if c==l:
#         print(True)
#     else:
#         print(False)

def sublist(l1,l2):
    def get_in_all(o,a):
        for el in o:
            if el in a:
                yield el
    
    for x1,x2 in zip(get_in_all(l1,l2),get_in_all(l2,l1)):
        if x1!=x2:
            return False
    
    return True

print(sublist(l1,l2))