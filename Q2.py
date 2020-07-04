# Write a python function stats() that takes name of text file as an argument. The function should print the number of lines, words, and characters in the file. For example,
# >>>stats('example.txt')
# Line count: 3
# Word count: 20
# Character count: 98

def stats(file):
    lc=wc=cc=0
    with open(file,'r') as f:
        for l in f:
            wl=l.split()
            lc+=1
            wc+=len(wl)
            cc+=len(l)
    return (lc,wc,cc)

lc,wc,cc=stats('examples.txt')

print(f'Line count: {lc}')
print(f'Word count: {wc}')
print(f'Character count: {cc}')