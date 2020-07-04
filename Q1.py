# Write a Python function named numVowels that is passed a string containing letters, each of which may be in either uppercase or lowercase, and returns a tuple containing the number of vowels and the number of consonants the string contains.

def numVowels(string):
    v=['a','e','i','o','u']
    c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    lc=lv=0
    for i in string:
        if i in v:
            lv+=1
        elif i in c:
            lc+=1
    return (lv,lc)

s=input("Enter a string containing letters : ")

vc,cc=numVowels(s.lower())
print(f"The number of vowels are {vc} and number of consonants are {cc} in the string '{s}'")