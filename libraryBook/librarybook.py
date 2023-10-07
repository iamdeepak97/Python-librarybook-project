class Library:
    def __init__(self,listofbooks):
        self.books = listofbooks
        
    def availablebooks(self):
        print("Books are available in this library.!! ")
        for book in self.books:
            print(" * " + book)
            
    def getbook(self,bookname):
        if bookname in self.books:
            print(f"you have been issued {bookname}.pls return it on time.!!")
            self.books.remove(bookname)
            return True
        else:
            print("sorry this book is not available or already has been issued to someone plz wait for it.!!")
            return False
        
    def returnbook(self,bookname):
        self.books.append(bookname)
        print("Thanks for giving! ")
        
class Student:
    def requestbook(self):
        self.book=input("Enter the name of the book you want to borrow!  ")
        return self.book
    def returnbook(self):
        self.book=input("Enter the name of the book you want to return or donate the book!  ")
        return self.book
    
Onlinelibrary=Library(["python",'bootstarp','c++','java','django','react','flask','restapi'])
student=Student()
while (True):
    welcomemsg='''\n =====welcome to library=====
    1. check available books
    2. borrow a book
    3. return or donate a book
    4. Exit the library
    '''
    print(welcomemsg)
    a=int(input("Enter a choice!  "))
    if a==1:
        Onlinelibrary.availablebooks()
    elif a==2:
        Onlinelibrary.getbook(student.requestbook())
    elif a==3:
        Onlinelibrary.returnbook(student.returnbook())
    elif a==4:
        print("Thanks for visiting library!!!")
        exit()
    else:
        print("Invalid choice!")