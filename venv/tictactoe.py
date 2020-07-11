
import random



def display (board) :
    print(board[0] + ' | '+ board[1] +' | '+ board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def inputs():
    choice = True

    while choice == True:
        user = input("Enter X or O for player 1: ").upper()
        if user == 'X':
            return ('X','O')
            choice =False

        elif user == 'O':
            return ('O','X')
            choice = False
        else:
            print("Try Again")


def position():

    first = random.randrange(0,2)
    placement = False

    if first == 0 :
        print("Player 1 goes first")
        return ('1')
    else :
        print("Player 2 goes first")
        return ('2')


def x(test_board):
    pos = position()
    sum = 0
    choice = "true"
    while choice =="true":
        if pos == '1':
            while sum < 9:

                user_1 = int(input("Player 1: Enter number from (1-10) to be placed on to the board :"))
                test_board[user_1] = 'X'
                sum = sum+1

                if sum >=9 or checking(test_board):
                    display(test_board)
                    choice = "false"
                    return True
                    break
                display(test_board)
                user_2 = int(input("Player 2: Enter number from (1-10) to be placed on to the board :"))
                test_board[user_2] = 'O'
                sum= sum+1

                display(test_board)

        elif pos == '2':
            user_2 = int(input("Player 2: Enter number from (1-10) to be placed on to the board :"))
            test_board[user_2] = 'O'
            sum = sum + 1

            if sum >= 9 or checking(test_board):
                display(test_board)
                choice = "false"
                return True
                break
            display(test_board)
            user_1 = int(input("Player 1: Enter number from (1-10) to be placed on to the board :"))
            test_board[user_1] = 'X'
            sum = sum + 1

            display(test_board)



def O(test_board):
    pos = position()
    sum = 0
    choice = "true"
    while choice == "true":
        if pos == '1':
            while sum < 9:

                user_1 = int(input("Player 1: Enter number from (1-10) to be placed on to the board :"))
                test_board[user_1] = 'O'
                sum = sum + 1

                if sum >= 9 or checking(test_board):
                    display(test_board)
                    choice = "false"
                    return True
                    break
                display(test_board)
                user_2 = int(input("Player 2: Enter number from (1-10) to be placed on to the board :"))
                test_board[user_2] = 'X'
                sum = sum + 1

                display(test_board)

        elif pos == '2':
            user_2 = int(input("Player 2: Enter number from (1-10) to be placed on to the board :"))
            test_board[user_2] = 'X'
            sum = sum + 1

            if sum >= 9 or checking(test_board):
                display(test_board)
                choice = "false"
                return True
                break
            display(test_board)
            user_1 = int(input("Player 1: Enter number from (1-10) to be placed on to the board :"))
            test_board[user_1] = 'O'
            sum = sum + 1

            display(test_board)

def checking(test_board):
    if test_board[0] == test_board[1] == test_board[2] or test_board[0] == test_board[4] == test_board[8] or test_board[0]==test_board[3]==test_board[6]:

        return True
    else:
        return False


test_board = [''] *9






win = False
display(test_board)

play = "Yes"

while play == "Yes":
    choice = inputs()

    player_1 = choice[0]
    player_2 = choice[1]

    if choice[0] == 'X':
        x(test_board)
        while checking(test_board) == False:

            checking(test_board)
            break
        if checking(test_board) == False:
            print("Draw")
        else:
            print("winner")

        user_1 = input("Want to play again ? (Y/N)")
        test_board = [''] * 9
        if user_1 == "N":
            play = "No"

    else:
        O(test_board)
        while checking(test_board) == False:

            checking(test_board)
            break
        if checking(test_board) == False:
            print("Draw")
        else:
            print("winner")

        user_1 = input("Want to play again ? (Y/N)")
        test_board = [''] * 9
        if user_1 == "N":
            play = "No"








