#Online menager system \
# create a libraray class
#use displaybook\
# lend book
# add book\
# return book
#Manilibrary=library(list ofbooks, library name)
#dictionary(book-namepersion)\
# create a main function and run an infinite while loop  asking user for their input
class library:
    def  __init__(self, bookoflist , libraryname):
        self.booklist=bookoflist
        self.libraryname=libraryname
        self.lend = {}

   def displaybook(self):
       print(self.bookoflist)

def addbook(self):
    books=input("Enter the book name:").capitalize()
    self.book=list.append(books)
def  lendbook(self):
    book=input("enter your book name:").capitalize()
    if book  not  in self.bookoflist:
        print("please enter validbook")
        if book  in self.bookoflist:
            name=input("Enter your name")
            self.bookoflist.remive(book)
            self.lend[book]=name
        else:
            if self.lend.get(book):
                print(f"book does not exsist by "
                      f"{self.lend[book]}")

def  returnbook(self):
    book=input("Enter book name").capitalize()
    if book in self.lend:
        self.bookoflist.append(book)
        del self.lend[book]
    else:
        print("enter the valid input")
    if __name__=='__main__':
        bookoflist=['c','c++','java','python']
maniket_library=library(bookoflist ,'maniket_library')
while  True:
    user=input("\nD - to display a book \nA-to add a book\nL-for lrnd a book\nR-to return  a  book\nQ-for exit()")
    if user=="Q" or user=="q" :
        break
    elif user =="Display" or user=="does.txt" or user =="D":
        maniket_library.displaybook()
    elif user == "Lend" or user == "l" or user == "L":
        maniket_library.lend()
    elif user =="Add" or user=="a" or user =="A":
        maniket_library.addbook()
    elif user =="return" or user=="r" or user =="R":
        maniket_library.returnbook()
