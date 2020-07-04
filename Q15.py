# Implement function partition() that splits a list of soccer players into two groups. More precisely, it takes a list of first names (strings) as input and prints the names of those soccer players whose first name starts with a letter between and including A and M.
# >>>partition(['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin'])
# Eleanor
# Evelyn
# Gavin
# >>> partition(['Xena', 'Sammy', 'Owen'])

def partition(l):
    s=[i.upper() for i in "abcdefghjikm"]
    # print(s)
    for i in l:
        if i[0] in s:
            print(i)
    
partition(['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin'])