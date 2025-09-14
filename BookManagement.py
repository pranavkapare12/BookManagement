from tabulate import tabulate

# CHECK IS BOOK IS PRESENT IN DICTONARY (DELETING) ITEMS
def isBookPresent(book,ID):
    if ID in book:
        return True
    return False

# CHECK IS BOOK_ID IS ALREADY IN DICTONARY
def IdAlreadyExist(bookId , book):
    if bookId in book:
        print(":: BOOK ID IS ALREADY PRESENT ::")
        return True
    else :
        return False

# RETURN A BOOK
def getBook(book_id,book):
    book_Title = input("ENTER TITLE OF BOOK :: ")
    book_Author = input("ENTER BOOK AUTHORE :: ")
    book_Price = input("ENTRE BOOK PRICE :: ")
    if not book_Price.isnumeric():
        print("Book Value Should be Float/integer Value")
        return
    book_Price = float(book_Price)
    book_Categorie = input("ENTER BOOK CATEGORIE :: ")
    book[book_id]={
        "Title":book_Title,
        "Author":book_Author,
        "Cate":book_Categorie,
        "Price":book_Price
        }
# ADD THE BOOK
def addBooks(book):
    while True:
        print('ENTER (STOP) in BOOK ID To Exit ')
        book_id = input("ENTER BOOK ID :: ")
        if not book_id.isnumeric():
            return
        if IdAlreadyExist(int(book_id),book):
            a=False
        else:
            getBook(int(book_id),book)

# DELETE BOOK FROM DICTONARY
def deleteBookById(book):
    ID = int(input("ENTER BOOK ID :: "))
    if(isBookPresent(book,ID)):
        del book[ID]
        print("DELETE SUCCESSFULLY")
    else:
        print("BOOK NOT FOUND")

def displayTable(mydict):
    new_dict = dict()

    for key,value in mydict.items():
        tempList = list()
        tempList.append(key)
        tempList.append(value['Title'])
        tempList.append(value['Author'])
        tempList.append(value['Cate'])
        tempList.append(value['Price'])
        new_dict[key]=tempList
    table = tabulate(new_dict.values(),
                     headers=["ID","Title","Author","Category","Price"]
                     ,
                     tablefmt = "fancy_grid"
                     )
    return table

# DISPLAY BOOK IN DICTONARY
def Display(book):
    table = displayTable(book)
    print(table)

def isPresent(book,key,searchValue):
    #print(key , book)
    #print(type(book[key]))
    if key in book:
        if isinstance(book[key], str) and book[key].lower() == searchValue:
            return True
        elif book[key] == searchValue:
            return True
        else:
            return
    else:
        print("Key is not Present Enter (Author,Title,Price)")
        return False



# SEARCH BOOK BY NAME
def Search(book):
    key = input("Enter by which type you wnat to search Book (title,autho,price)::")
    searchValue = input("Enter Search Value :: ")
    searchValue = searchValue.lower()
    key = key.lower().capitalize()
    if key == 'Price':
        searchValue = float(searchValue)
    else:
        key = key.lower().capitalize()
    for keys,value in book.items():
        if(isPresent(value,key,searchValue)):
            print("*"*30)
            print("Book Id :: ",keys)
            for listValue in value:
                print(listValue ," :: ", value[listValue])
            print("*"*30)

def updateBook(book):
    book_id = input("Enter Book Id (MUST NUMERIC isnumeric):: ")
    if not book_id.isnumeric():
        print("Book Id Must be Numeric")
        return
    book_id = int(book_id)
    if not book_id in book:
        print("Book is not Present")
        return
    new_book = book[book_id]
    key = input('Enter by which type you wnat to search Book (title,autho,price,cate(Catagorie))::')
    key = key.lower().capitalize()
    value = input('Enter new Value :: ')
    if (key == 'price'):
        value = float(value)
    else:
        value = value.lower().capitalize()
    new_book[key]= value

def searchByAuthore(Bdic):
    Authore = input("Enter Authore Name :: ")
    Authore = Authore.lower()
    displayList = list()
    table = ""
    count = 0
    for key,value in Bdic.items():
        if value['Author'].lower() == Authore:
            count += 1
            table = str(key)+"\t"+value['Title']+"\t"+value['Author']+"\t"+value['Cate']+"\t"+str(value['Price'])
            displayList.append(table.split('\t'))
    if count == 0:
        print("No Record Found")
        return
    table= "Count \t"+str(count)
    displayList.append(table.split('\t'))
    headers = ['ID','NAME','AUTHORE','CATEGORY','PRICE']
    print(tabulate(displayList,headers=headers))
    return

def TypeWise(Bdic):
    Cate = input("ENTER CATEGORIE :: ")
    Cate = Cate.lower()
    displayList = list()
    table = ""
    count = 0
    for key,value in Bdic.items():
        if value['Cate'].lower() == Cate:
            count += 1
            table = str(key)+"\t"+value['Title']+"\t"+value['Author']+"\t"+value['Cate']+"\t"+str(value['Price'])
            displayList.append(table.split('\t'))
    if count == 0:
        print("No Record Found")
        return
    table= "Count \t"+str(count)
    displayList.append(table.split('\t'))
    headers = ['ID','NAME','AUTHORE','CATEGORY','PRICE']
    print(tabulate(displayList,headers=headers))
    return

def maxPrice(mydict):
    string = ""
    setPrice = True
    ids = 0
    for key,value in mydict.items():
        if setPrice:
            setPrice = False
            maxPrice = value['Price']
            ids = key
            string = str(key)+"\t"+value['Title']+"\t"+value['Author']+'\t'+value['Cate']+"\t"+str(value['Price'])
            continue
        if value['Price'] > maxPrice:
            maxPrice = value['Price']
            ids = key
            string = str(key)+"\t"+value['Title']+"\t"+value['Author']+'\t'+value['Cate']+"\t"+str(value['Price'])

    return string,maxPrice,ids

def findNMax(mydic,val,ids):
    flag = True
    ke = -1
    for key,value in mydic.items():
        if flag and key not in ids:
            ke = key
            string = str(key)+"\t"+value['Title']+"\t"+value['Author']+'\t'+value['Cate']+"\t"+str(value['Price'])
            minPrice = value['Price']
            flag = False
        elif not flag and minPrice < value['Price'] and key not in ids:
            #print(value)
            minPrice = value['Price']
            string = str(key)+"\t"+value['Title']+"\t"+value['Author']+'\t'+value['Cate']+"\t"+str(value['Price'])
            ke = key
    ids.append(ke)
    #print("Min Price is"+str(minPrice))
    return string,minPrice
            

def higestPrice(mydict):
    ids = list()
    displayList = list()
    # for Validation Only
    value = input("Enter Integer Value")
    if not value.isnumeric():
        print("Please Enter Integer Value")
        return
    value = int(value)
    length = len(mydict)
    if value > length:
        print("The Value is Greater than dictonary Size")
        return
    #-------------------#
    # Finding Max Price in the Dictonary
    table = str()
    table,num,book_id = maxPrice(mydict)
    displayList.append(table.split('\t'))
    ids.append(book_id)
    value -= 1

    # now finding the value which is Second higest in dictonary
    while value > 0:
        string,num = findNMax(mydict,num,ids)
        table = string
        displayList.append(table.split('\t'))
        value -= 1
    headers = ['ID','NAME','AUTHORE','CATEGORY','PRICE']
    print(tabulate(displayList,headers=headers))
    print(ids)

def displayMenu():
    print('''
Press (1) :: ADD BOOK
Press (2) :: UPDATE BOOK
Press (3) :: DELETE ENTRY
Press (4) :: DISPLAY BOOKS
Press (5) :: SEARCH BOOK
Press (6) :: EXIT
Press (7) :: SEARCH BY AUTHORE
Press (8) :: SEARCH BY CATEGORIE
Press (9) :: SORT HIGEST PRICE
''')



def main():
    book = {
    1: {'Title': 'Let Us C', 'Author': 'Yashavant Kanetkar', 'Cate': 'Coding', 'Price': 3000.0},
    2: {'Title': 'C Programing Language', 'Author': 'Dennis Ritchie', 'Cate': 'Coding', 'Price': 2000.0},
    3: {'Title': 'Dot Net', 'Author': 'Dennis Ritchie', 'Cate': 'Coding', 'Price': 500.0},
    4: {'Title': 'Java Programing', 'Author': 'Dennis Ritchie', 'Cate': 'Coding', 'Price': 1000.0},
    5: {'Title': 'The Hitchhiker\'s Guide to Python', 'Author': 'Kenneth Reitz', 'Cate': 'Coding', 'Price': 1500.0},
    6: {'Title': 'Automate the Boring Stuff with Python', 'Author': 'Al Sweigart', 'Cate': 'Coding', 'Price': 850.0},
    7: {'Title': 'Pride and Prejudice', 'Author': 'Jane Austen', 'Cate': 'Classic', 'Price': 350.0},
    8: {'Title': 'To Kill a Mockingbird', 'Author': 'Harper Lee', 'Cate': 'Classic', 'Price': 400.0},
    9: {'Title': 'Dune', 'Author': 'Frank Herbert', 'Cate': 'Sci-Fi', 'Price': 925.0},
    10: {'Title': '1984', 'Author': 'George Orwell', 'Cate': 'Classic', 'Price': 450.0},
    11: {'Title': 'The Lord of the Rings', 'Author': 'J.R.R. Tolkien', 'Cate': 'Fantasy', 'Price': 2800.0},
    12: {'Title': 'Sapiens: A Brief History of Humankind', 'Author': 'Yuval Noah Harari', 'Cate': 'History', 'Price': 1100.0},
    13: {'Title': 'The Martian', 'Author': 'Andy Weir', 'Cate': 'Sci-Fi', 'Price': 750.0},
    14: {'Title': 'The Silent Patient', 'Author': 'Alex Michaelides', 'Cate': 'Thriller', 'Price': 600.0},
    15: {'Title': 'The Girl with the Dragon Tattoo', 'Author': 'Stieg Larsson', 'Cate': 'Thriller', 'Price': 700.0},
    16: {'Title': 'Educated', 'Author': 'Tara Westover', 'Cate': 'Memoir', 'Price': 800.0},
    17: {'Title': 'Where the Crawdads Sing', 'Author': 'Delia Owens', 'Cate': 'Fiction', 'Price': 675.0},
    18: {'Title': 'The Hunger Games', 'Author': 'Suzanne Collins', 'Cate': 'YA Fiction', 'Price': 550.0},
    19: {'Title': 'Harry Potter and the Sorcerer\'s Stone', 'Author': 'J.K. Rowling', 'Cate': 'Fantasy', 'Price': 900.0},
    20: {'Title': 'The Da Vinci Code', 'Author': 'Dan Brown', 'Cate': 'Thriller', 'Price': 820.0}
}
    while True:
        displayMenu()
        switch = input('-> ')
        if not switch.isnumeric():
            print("The Value must be numeric")
            continue
        switch = int(switch)
        
        if switch == 1:
            addBooks(book)
        elif switch == 2:
            updateBook(book)
        elif switch == 3:
            deleteBookById(book)
        elif switch == 4:
            Display(book)
            #displayTable(book)
        elif switch == 5:
            Search(book)
        elif switch == 6:
            return
        elif switch == 7:
            searchByAuthore(book)
        elif switch == 8:
            TypeWise(book)
        elif switch == 9:
            higestPrice(book)
        else:
            print("INVALID OPTION")
        
main()
