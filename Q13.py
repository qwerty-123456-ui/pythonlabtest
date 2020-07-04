# Create a dictionary for words and their meanings. Write functions to add a new entry (word:meaning) ,search for a particular word and retrieve meaning, given meaning find words with same meaning , remove an entry, display all words sorted alphabetically. [Program must be menu driven]

word_dict={}

def Create_dict():
    global word_dict
    word_dict={}
    ch="y"
    while (ch=='y') or (ch=="Y"):
        print("\nEnter word : ",end="")
        word=input()
        print("\nEnter meaning : ",end="")
        meaning=input()
        word_dict[word]=meaning
        print("Do want to continue adding word and meaning (y or n) ? \n",end="")
        ch=input()

def add_word():
    global word_dict
    print("\nEnter word: ",end="")
    word=input()
    print("\nEnter meaning: ",end="")
    meaning=input()
    word_dict[word]=meaning

def find_meaning(w):
    return word_dict[w]

def find_word_same_meaning(mng):
    words=[]
    for w,m in word_dict.items():
        if mng==m:
            words.append(w)
    return words

def display_sorted():
    for w,m in word_dict.items():
        print(f"{w} ==> {m}")
    print("Sorted list : ")
    print(sorted(word_dict.keys()))

def main():
    ch="y"
    while ch.lower()=="y":
        print("1. Create new dictionary\n2. Add new word\n3. Find meaning\n4. Find word with same meaning\n5. Display sorted list of words\nEnter choice : ",end="")
        option=int(input())
        if option==1:
            Create_dict()
        elif option==2:
            add_word()
        elif option==3:
            print("Enter word : ",end="")
            word=input()
            print("Meaning  : ",find_meaning(word))
        elif option==4:
            print("Enter meaning : ")
            mng=input()
            print("Words with same meaning are : ",end="")
            print(find_word_same_meaning(mng))
        elif option==5:
            display_sorted()
        print("\nDo you want to continue  (y or n)?",end="")
        ch=input()

if __name__=="__main__":
    main()

