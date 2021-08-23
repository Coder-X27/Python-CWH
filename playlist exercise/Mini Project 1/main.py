# class Library():
#     def __init__(self,user):
#         self.user=user
#     def add(self,lis1):
#         print('Add function')
#         print(lis1)
#         newbook=input('Enter the name of the book\n')
#         lis1.append(newbook)
#         print('The updated list is ',lis1)

#     def show(self,lis1):
#         for item in lis1:
#             print(item)

#     def lend(self):
#         print('Lend function')

#     def ret(self):
#         print('Return function')

# def main():
#     while(True):
#         user=input('What is your name\n')
#         # book=input('Book name\n')
#         choice=int(input('1.) Add Book\n2.) Show Book\n3.) Return Book\n4.)Lend Book\n'))
#         lis1=['Spiderman','Superman','Batman','IronMan']
#         first=Library(user)
#         # print('The list Before the add function ',lis1)
#         if choice==1:
#             first.add(lis1)
#             a=lis1
#         elif choice==2:
#             first.show(lis1)
#         elif choice==3:
#             first.ret()
#         elif choice==4:
#             first.lend()
#         else:
#             print('Enter a valid character')
#         exit=input("Do you watned to exit yes or no !\n")
#         if exit=='yes':
#             print('Thank you for using this library ! ')
#             break
#         else:
#             print("This programme is running again ")
    
# if __name__ == '__main__':
#     main()
    
# class Library():
#     def __init__(self,list_of_books,Library_name):
#         # creating a dictionary of all books keys
#         self.lend_data = {}
#         self.list_of_books = list_of_books
#         self.library_name = Library_name

#         # adding books to dictionary
#         for books in self.list_of_books:
#             # none means No reader have lend this book
#             self.lend_data[books] = None

#     def display_books(self):
#         for index,books in enumerate(self.list_of_books):
#             print(f"{index+1}:{books}")

#     def lend_book(self,book,reader):
#         if book in self.list_of_books:
#             if self.lend_data[book] is None:
#                 self.lend_data[book] = reader
#                 print("Book Lend")
#             else:
#                 print(f"Sorry This book is lend by {self.lend_data[book]}")
#         else:
#             print("You have written wrong book name")

#     def return_book(self,book,reader):
#         if book in self.list_of_books:
#             if self.lend_data[book] is not None:
#                 self.lend_data.pop(book)
#             else:
#                 print("Sorry but This book is not Lend")
#         else:
#             print("You have written wrong book name")

#     def add_book(self,book_name):
#         self.list_of_books.append(book_name)
#         self.lend_data[book_name] = None

#     def delete_book(self,book_name):
#         self.list_of_books.remove(book_name)
#         self.lend_data.pop(book_name)

# def main():
#     # By deafault variables
#     list_books = ['Cookbook','Sherlock Holmes','Chacha_chaudhary','Rich Dad and Poor Dad']
#     Library_name = 'Harry'
#     secret_key = 123456

#     Harry = Library(list_books,Library_name)

#     print(f"Welecome To {Harry.library_name} library\n\nq for exit \nDisplay Book Using 'd' and add lend book using 'l' and Return a Book using 'r' \nAdd Book Using 'a' and Delete Book using 'del' \n ")

#     Exit = False
#     while (Exit is not True):
#         _input = input("option:")
#         print("\n")
        
#         if _input == "q":
#             Exit = True

#         elif _input == "d":
#             Harry.display_books()

#         elif _input == "l":
#             _input2 = input("What is your name:")
#             _input3 = input("Which Book Do you want to lend:")
            
#             Harry.lend_book(_input3,_input2)

#         elif _input == "a":
#             _input2 = input("Book name:")
#             Harry.add_book(_input2)

#         elif _input == "del":
#             _input_secret = int(input("Write the secret key to delete:"))
#             if (_input_secret == secret_key):
#                 _input2 = input("Book Which you want to delete:")
#                 Harry.delete_book(_input2)
#             else:
#                 print("Sorry We can't Delete the Book")

#         elif _input == "r":
#             _input2 = input("What is your name:")
#             _input3 = input("Which Book Do you want to return:")
#             Harry.return_book(_input3,_input2)

# if __name__ == "__main__":
#     main()

board = [' ' for x in range(10)]

def insertLetter(letter,pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while run:
        move = input("please select a position to enter the X between 1 to 9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')

        except:
            print('Please type a number')

def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the game!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(IsWinner(board , 'O')):
            playerMove()
            printBoard(board)
        else:
            print("sorry you loose!")
            break

        if not(IsWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('computer placed an o on position' , move , ':')
                printBoard(board)
        else:
            print("you win!")
            break




    if isBoardFull(board):
        print("Tie game")

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
