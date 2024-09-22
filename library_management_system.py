class Library:
    def __init__(self,list,name):
        self.booksList=list
        self.name=name
        self.lendDict={}#dictionary
    def displayBooks(self):
        print(f"We havefollowing books in our library:{self.name}")
        for book in self.booksList:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print(f"lender book database has been updated.you can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
    def addBook(self,book):
        self.booksList.append(book)
        print(f"book has been added to the book list")
    def returnBook(self,book):
        self.lendDict.pop(book)
if __name__=='__main__':
    NITESH=Library(["Python","Rich Daddy Poor Daddy","Harry Potter","C++ Basics","Algorithm by CLRS"],"NITESH AGRAHARI")
    while(True):
        print(f"Welcome to the {NITESH.name} library.Enter your choice to continue")
        print("1.Display Book")
        print("2.Lend a Book")
        print("3.Add a Book")
        print("4.Return a Book")
        user_choice=input()
        if user_choice not in ["1","2","3","4"]:
            print("Enter the right choice")
            continue
        else:
            user_choice=int(user_choice)

        if user_choice==1:
            NITESH.displayBooks()
        elif user_choice==2:
            book=input("Enter the name that you want to lend:")
            user=input("Enter your name")
            NITESH.lendBook(user,book)
        elif user_choice==3:
            book=input(f"Enter the name of book that you want to add:")
            NITESH.addBook(book)
        elif user_choice==4:
            book=input(f"Enter the name of book that you want to return:")
            NITESH.returnBook(book)
        else:
            print(f"Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2=""
        while(user_choice2!="c" and user_choice2!="q"):
          user_choice2=input()
          if user_choice2=="q":
            exit()
          elif user_choice2=="c":
              continue














