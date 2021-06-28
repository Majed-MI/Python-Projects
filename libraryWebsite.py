# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

# defining class library
class Library:
    # constructor for the class
    def __init__(self, list, name):
        # two values taking
        self.booksList = list
        self.name = name
        # one empty dictionary taken which will be listed when a lend book is done
        self.lendDict = {}

    #displaying booklist
    def displayBooks(self):
        # library name is included and the following book will also be shown
        print(f"We have following books in our library: {self.name}")
        # displaying booklist one by one
        for book in self.booksList:
            print(book)

    # lend book function taking two values
    def lendBook(self, user, book):
        # if book is not in lend dictionary list then the entry would be done and update too
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        # if the book is in lend dictionary list then the lender name will be shown
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    # adding book function
    def addBook(self, book):
        # adding book in the booklist
        self.booksList.append(book)
        print("Book has been added to the book list")

    # returning book function
    def returnBook(self, book):
        # removing the book from lend dictionary list
        self.lendDict.pop(book)

if __name__ == '__main__':
    # instance var = function(booklist,name)
    majed = Library(['Python', 'Circuit Master', 'Creative thinking', 'JavaScript : Web Design', 'Mathematics : Integration'], "Iftekhar")

    # while loop to continue
    while(True):
        # displaying book
        print(f"Welcome to the {majed.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        # taking input 1/2/3/4 from user
        user_choice = input()
        # if invalid then continue again
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            majed.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            majed.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            majed.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            majed.returnBook(book)

        else:
            print("Not a valid option")

        # continue or quit
        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            # if q is the choice for the user then just exit
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue