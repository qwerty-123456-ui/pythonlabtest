# Write a python function vowelCount() that takes a string as input and counts number of occurrences of each vowels in the string. For. Eg.
# >>>vowelCount('Le Tour de France')
# a, e, i, o, and u appear, respectively, 1, 3, 0, 1, 1 times

def vowelCount(string):
    print(f"a, e, i, o, and u appear, respectively, {string.count('a')}, {string.count('e')}, {string.count('i')}, {string.count('o')}, {string.count('u')} times ")
    # string=string.casefold()
    # print(string)
    # count={}.fromkeys("aeiou",0)
    # print(count)

vowelCount('Varun Cornelio'.lower())
