# import time
# import random


library_text = r"""
 _     _ _                          
| |   (_) |                         
| |    _| |__  _ __ __ _ _ __ _   _ 
| |   | | '_ \| '__/ _` | '__| | | |
| |___| | |_) | | | (_| | |  | |_| |
\_____/_|_.__/|_|  \__,_|_|   \__, |
                               __/ |
                              |___/ 
      """
settings_text = r"""
 _____      _   _   _                 
/  ___|    | | | | (_)                
\ `--.  ___| |_| |_ _ _ __   __ _ ___ 
 `--. \/ _ \ __| __| | '_ \ / _` / __|
/\__/ /  __/ |_| |_| | | | | (_| \__ \
\____/ \___|\__|\__|_|_| |_|\__, |___/
                             __/ |    
                            |___/     
"""
load_text = r"""
 _                     _     ______             _    
| |                   | |    | ___ \           | |   
| |     ___   __ _  __| |    | |_/ / ___   ___ | | __
| |    / _ \ / _` |/ _` |    | ___ \/ _ \ / _ \| |/ /
| |___| (_) | (_| | (_| |    | |_/ / (_) | (_) |   < 
\_____/\___/ \__,_|\__,_|    \____/ \___/ \___/|_|\_\
                                                                                                   
"""

class Database:
  def __init__(self, path):
    self.path = path
    file = open(path, 'r')
    self.num_books = int(file.readline())
    self.books = []
    for x in range(self.num_books):
        self.books.append(Book(file.readline(),file.readline(),file.readline(),file.readline(),file.readline()))
    file.close()

  def append_book(self,book):
    self.num_books = self.num_books+1
    file = open(self.path, "w")
    file.write(str(self.num_books)+"\n")
    file.close()
    file = open(self.path, 'a')
    self.books.append(book)
    for x in range(self.num_books):
        file.write(self.books[x].title)
        file.write(self.books[x].author)
        file.write(self.books[x].date)
        file.write(self.books[x].rating)
        file.write(self.books[x].review)
    file.write("\n")
    file.close()

class Book:
  def __init__(self, title, author, date, rating, review):
    self.title = title
    self.author = author
    self.date = date
    self.rating = rating
    self.review = review
  def set_default(self):
    if (self.title ==None):
        self.title = "Unset Title"
    if (self.author ==None):
        self.author = "Unknown Author"
    if (self.date ==None):
        self.date = "0/00/0000"
    if (self.rating ==None):
        self.rating = "Unknown Rating"
    if (self.review ==None):
        self.review = "Empty Review"

def read_book(database):
    print(load_text)
    repeat=0
    while(repeat == 0):
        file_path = input("Enter the file path to the book you want to upload. Note: there is currently no way to remove books from the library. Type E to exit\n: ")
        if(file_path=="E"):
            return 0
        try:
            with open(file_path, 'r') as file:
                book_title = (file.readline())
                print(f"Book successfully found at location {file_path}!")
                print(book_title)
                file.close()
                repeat2 =0
                while(repeat2==0):
                    upload = input("Upload?(Y/N)\n")
                    if upload == "Y":
                        repeat=1
                        repeat2=1
                    if upload == "N":
                        repeat2=1   
        except FileNotFoundError:
            print(f"No book found at {file_path} \n Please try again")
    repeat =0
    file = open(file_path, 'r')
    book = Book(file.readline(),file.readline(),file.readline(),file.readline(),file.readline())
    file.close()
    while(repeat==0):
        NULL_VAL = input("Would you like to replace any NULL values with defaults?(Y/N): WARNING, leaving NULL values in can have negative effects. It's recomended to choose Y\n:")
        if NULL_VAL == "Y":
            repeat=1
            book.set_default()
        if NULL_VAL == "N":
            repeat=1
    database.append_book(book)
    while(0==0):
        exit = input("Book uploaded! Type E to return to the library\n:")
        if(exit=="E"):
            return 0


def settings(database):
    print(settings_text)
    repeat=0
    while(repeat == 0):
        file_path = input("Enter the file path to the book you want to upload. Note: there is currently no way to remove books from the library. Type E to exit\n: ")
        if(file_path=="E"):
            return 0
        try:
            with open(file_path, 'r') as file:
                book_title = (file.readline())
                print(f"Book successfully found at location {file_path}!")
                print(book_title)
                file.close()
                repeat2 =0
                while(repeat2==0):
                    upload = input("Upload?(Y/N)\n")
                    if upload == "Y":
                        repeat=1
                        repeat2=1
                    if upload == "N":
                        repeat2=1   
        except FileNotFoundError:
            print(f"No book found at {file_path} \n Please try again")
    repeat =0
    file = open(file_path, 'r')
    book = Book(file.readline(),file.readline(),file.readline(),file.readline(),file.readline())
    file.close()
    while(repeat==0):
        NULL_VAL = input("Would you like to replace any NULL values with defaults?(Y/N): WARNING, leaving NULL values in can have negative effects. It's recomended to choose Y\n:")
        if NULL_VAL == "Y":
            repeat=1
            book.set_default()
        if NULL_VAL == "N":
            repeat=1
    database.append_book(book)
    while(0==0):
        exit = input("Book uploaded! Type E to return to the library\n:")
        if(exit=="E"):
            return 0











database= Database("C:\\Users\\tebbu\\Desktop\\CS\\CS361\\main\\database.txt")



read_book(database)