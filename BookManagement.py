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
    book_Price = float(input("ENTRE BOOK PRICE :: "))
    book[book_id]={
        "Title":book_Title,
        "Author":book_Author,
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
    
# DISPLAY BOOK IN DICTONARY
def Display(book):
    print("*"*10,end=" ")
    print("--BOOKS--","*"*10)
    for key,value in book.items():
        print("*"*30)
        print("BOOK ID :: ",key)
        for val in value:
            print(val.upper()," :: ",value[val])
    print("*"*30)

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
    key = input('Enter by which type you wnat to search Book (title,autho,price)::')
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
    table = "BookId\tTitle\t\tAuthor\t\tPrice\n"
    count = 0
    for key,value in Bdic.items():
        if value['Author'].lower() == Authore:
            count += 1
            table += str(key)+"\t"+value['Title']+"\t"+value['Author']+"\t"+str(value['Price'])+"\n"
            #print("Book Id ::"+str(key)+" Title :: "+value['Title']+" Authore :: "+value['Author']+" Price :: "+ str(value['Price']))
    if count == 0:
        print("No Record Found")
        return
    table+= "Count::"+str(count)
    print(table)
    return


def main():
    book = dict({
        1 : {'Title': 'Let Us C', 'Author': 'Yashavant Kanetkar', 'Price': 3000.0},
        2 : {'Title': 'C Programing Language', 'Author': 'Dennis Ritchie', 'Price': 2000.0},
        3 : {'Title': 'Dot Net', 'Author': 'Dennis Ritchie', 'Price': 500.0},
        4 : {'Title': 'Java Programing', 'Author': 'Dennis Ritchie', 'Price': 1000.0}
        })
    while True:
        switch = int(input('Press (1) :: ADD BOOK \nPress (2) :: UPDATE BOOK \nPress (3) :: DELETE ENTRY \nPress (4) :: DISPLAY BOOKS \nPress (5) :: SEARCH BOOK \nPress (6) :: EXIT \nPress (7) Search By Authore \n -> '))
        if switch == 1:
            addBooks(book)
        elif switch == 2:
            updateBook(book)
        elif switch == 3:
            deleteBookById(book)
        elif switch == 4:
            Display(book)
        elif switch == 5:
            Search(book)
        elif switch == 6:
            return
        elif switch == 7:
            searchByAuthore(book)
        else:
            print("INVALID OPTION")
        
main()
