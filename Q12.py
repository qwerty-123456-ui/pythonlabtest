# Create a dictionary program that initializes a set of items and prices for it. Add methods to 1) get the price of an item.    2) display all the items in sorted order

item_dict={"Pen":10,"Pencil":5,"Eraser":3,"Sharpner":4,"Compass":20,"Notebook":50}

def add_dict():
    global item_dict
    ch="y"
    while (ch=='y') or (ch=="Y"):
        print("\nEnter item : ",end="")
        item=input()
        print("\nEnter  price : ",end="")
        price=input()
        item_dict[item]=price
        print("Do want to continue adding item and  price (y or n) ? \n",end="")
        ch=input()

def getPrice(item):
    if item in item_dict:
        return item_dict.get(item)
    else:
        return "Item not there"


def display_sorted():
    print("\nSorted list : ")
    print(sorted(item_dict.keys()))

    print("\nSorted dict : ")
    print("{",end="")
    for i in sorted(item_dict.keys()):
        print(f"'{i}:{item_dict[i]},",end=" ")
        
    print("}")

def main():
    ch="y"
    while ch.lower()=="y":
        print("1. Add to dictionary\n2. Get the price of an item \n3. Display sorted list of words\nEnter choice : ",end="")
        option=int(input())
        if option==1:
            add_dict()
        if option==2:
            print("Enter item : ",end="")
            item=input()
            print("Price : ",getPrice(item))
        elif option==3:
            display_sorted()
        print("\nDo you want to continue  (y or n)?",end="")
        ch=input()

if __name__=="__main__":
    main()

