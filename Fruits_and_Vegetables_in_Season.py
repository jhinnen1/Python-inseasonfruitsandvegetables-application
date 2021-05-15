# gets winter fruits/vegetables list from Winter.txt
def getWinterList():
    inFile = open( "Winter.txt", "r" )
    fruitSeq = inFile.read().splitlines()
    print(fruitSeq)
    inFile.close()
    print(" ")
    return

# gets spring fruits/vegetables list from Spring.txt
def getSpringList():
    inFile = open( "Spring.txt", "r" )
    fruitSeq = inFile.read().splitlines()
    print(fruitSeq)
    inFile.close()
    print(" ")
    return

# gets summer fruits/vegetables list from Summer.txt
def getSummerList():
    inFile = open( "Summer.txt", "r" )
    fruitSeq = inFile.read().splitlines()
    print(fruitSeq)
    inFile.close()
    print(" ")
    return

# gets fall fruits/vegetables list from Fall.txt
def getFallList():
    inFile = open( "Fall.txt", "r" )
    fruitSeq = inFile.read().splitlines()
    print(fruitSeq)
    inFile.close()
    print(" ")
    return

# function that creates a list data structure for a shopping list
def createShoppingList():
    print("You may also add other items such as Bread and Milk to your list.")
    shoppingList = []
    newItem = input("Enter your first item: ")
    sentinel = "Done"
    # while loop that adds items to the shopping list
    while newItem != sentinel:
        shoppingList.append ( newItem )
        newItem = input("Enter your next item or type 'Done' when finished: ")
    else:
        outFile = open( "Shopping List.txt", "w" )
        print((shoppingList), file=outFile)
        print(" ")
        print("Your shopping list has been created and you may print it or save it to your smartphone now!")


def main():
      
    print("This program is designed to give you a list of fruits and vegetables that are in season for a given month.")
    print("When buying fruits and vegetables that are in season you are getting them when they taste the best.")
    print("Therefore, promoting consumption of more fruits and vegetables in one's diet.")
    print(" ")
    month = input("Please enter the month for a list of fruits and vegetables that will taste great? ")
    print(" ")
    
    # elif statement to match a month with the appropriate fruits/vegetables list
    if (month == "December" or month == "January" or month == "February"):
        getWinterList()        
    elif (month == "March" or month == "April" or month == "May"):
        getSpringList()        
    elif (month == "June" or month == "July" or month == "August"):
        getSummerList()
    elif (month == "September" or month == "October" or month == "November"):
        getFallList()
        
    answer = input("Would you like to create a shopping list of these items? Enter 'Sure' (or) 'No Thanks': ")
    print(" ")
    
    # elif statement that calls the function to create a shopping list
    if (answer == "No Thanks"):
        print("Okay, but you're missing out on good food and a healthier lifestyle!")
    elif (answer == "Sure"):
        createShoppingList()  
               
      
main()