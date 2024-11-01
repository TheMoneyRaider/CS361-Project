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
  def __init__(self, path, path2):
    self.path = path
    self.settings_path = path2
    file = open(path, 'r')
    self.num_books = int(file.readline())
    self.books = []
    for x in range(self.num_books):
        self.books.append(Book(file.readline(),file.readline(),file.readline(),file.readline(),file.readline()))
    file.close()
    file = open(path2, 'r')
    self.settings = []
    for x in range(14):
        self.settings.append(int(file.readline()[0]))

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


  def settings_reset(self):
    file = open(self.settings_path, 'w')
    file.writelines(["0\n","0\n","0\n","1\n","1\n","1\n","1\n","1\n","0\n","0\n","1\n","0\n","0\n","0"])
    file.close()

  def update_settings(self):
    file = open(self.settings_path, 'w')
    file.writelines([str(self.settings[0])+"\n",str(self.settings[1])+"\n",str(self.settings[2])+"\n",str(self.settings[3])+"\n",str(self.settings[4])+"\n",str(self.settings[5])+"\n",str(self.settings[6])+"\n",str(self.settings[7])+"\n",str(self.settings[8])+"\n",str(self.settings[9])+"\n",str(self.settings[10])+"\n",str(self.settings[11])+"\n",str(self.settings[12])+"\n",str(self.settings[13])])
    file.close

  def print_settings(self):
      if(self.settings[0]==0):
        string1="Progress"
      else:
        string1="[Progress]"
      if(self.settings[1]==0):
        string2="Alphabetical"
      else:
        string2="[Alphabetical]"
      if(self.settings[2]==0):
        string3="Author"
      else:
        string3="[Author]"
      if(self.settings[3]==0):
        string4="Date"
      else:
        string4="[Date]"
      print(f"(S): Sorting Order    {string1} {string2} {string3} {string4}")
      if(self.settings[4]==0):
        string1="Title"
      else:
        string1="[Title]"
      if(self.settings[5]==0):
        string2="Rating"
      else:
        string2="[Rating]"
      if(self.settings[6]==0):
        string3="Review"
      else:
        string3="[Review]"
      if(self.settings[7]==0):
        string4="Author"
      else:
        string4="[Author]"
      if(self.settings[8]==0):
        string5="Status"
      else:
        string5="[Status]"
      if(self.settings[9]==0):
        string6="Progress"
      else:
        string6="[Progress]"
      print(f"(D): Display          {string1} {string2} {string3} {string4} {string5} {string6}")
      if(self.settings[10]==0):
        string1="5"
      else:
        string1="[5]"
      if(self.settings[11]==0):
        string2="10"
      else:
        string2="[10]"
      if(self.settings[12]==0):
        string3="15"
      else:
        string3="15]"
      if(self.settings[13]==0):
        string4="20"
      else:
        string4="[20]"
      print(f"(S): Books per page   {string1} {string2} {string3} {string4}")
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
    repeat=0
    while(repeat == 0):
        print(load_text)
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
    repeat=0
    while(repeat == 0):
        # Print(.....)
        print(settings_text)
        database.print_settings()
        user_input = input("Type the () letter followed by the number you wish to activate (i.e type S1 to set the sorting order to your progress in reading each book). Type E to exit the settings. type RESET to change the settings to default.\n: ")
        if(user_input=="E"):
            return 0
        elif(user_input=="RESET"):
            database.settings_reset()
        
        if(len(user_input)==2 and user_input[1].isnumeric()):
            if(user_input[0]=="S"):
                current_int=int(user_input[1])
                if(int(current_int)<5 and int(current_int)>0):
                    database.settings[0],database.settings[1],database.settings[2],database.settings[3]=0,0,0,0
                    database.settings[current_int-1]=1
                    database.update_settings()
            elif(user_input[0]=="D"):
                current_int=int(user_input[1])
                if(int(current_int)<7 and int(current_int)>0):
                    if(database.settings[current_int+3]==0):
                        database.settings[current_int+3]=1
                    else:
                        database.settings[current_int+3]=0
                    database.update_settings()
            elif(user_input[0]=="B"):
                current_int=int(user_input[1])
                if(int(current_int)<5 and int(current_int)>0):
                    database.settings[10],database.settings[11],database.settings[12],database.settings[13]=0,0,0,0
                    database.settings[current_int+9]=1
                    database.update_settings()
            











database= Database("C:\\Users\\tebbu\\Desktop\\CS\\CS361\\main\\database.txt","C:\\Users\\tebbu\\Desktop\\CS\\CS361\\main\\settings.txt")


settings(database)

# read_book(database)