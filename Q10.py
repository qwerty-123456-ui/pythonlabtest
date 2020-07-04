# Write a python function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok). How many abecedarian words are there?

def is_abecedarian(word):
    index = 0
    while index < len(word) -1:
        if word[index] > word[index+1]:
            return False
        else:
            index +=1
    return True

line=input("Enter the string : ")

c=0
print("Abecedarian words are : ")
for i in line.split():
    if is_abecedarian(i):
        print(i)
        c+=1

print(is_abecedarian("acdefgh"))
print(f"The number of abecedarian words in '{line}' are {c}")