#Benjamin Andrews
#Rock, Paper, Scissors Game
#User 1 will either play a rock, paper, scissors game
#against Computer 1, inputting their choice.
#Or User 1 will play a rock, paper, scissors game
#against User 2, each inputting their choice
import random #Allows the computer to choose

def main():
    #Initialize the main menu selection variables here
    menuSelection = 0 #Initialize the selection variable
    showMenu = 0
    startAgain = ""

    #Display initial menu statements
    print("_______________________________________________________")
    print("\tWelcome to Rock, Paper, Scissors Game!")
    print("")
    print ("\t\t\tMenu")
    print("-------------------------------------------------------")
    print ("1. Rules")
    print ("2. One-player vs Computer game")
    print ("3. Two-player game")
    print ("4. Restart/Quit\n")

    #get selection from user
    selection = eval(input("Please choose an option: "))

    #Begin decision structure
    if selection == 1:
        #call introduction and menu options
        showMenu = displayMenu(menuSelection, startAgain)
    elif selection == 2: #play with computer option
        playWithComputer(startAgain)
    elif selection == 3: #play with player option
        playWithPlayer(startAgain)
    elif selection == 4:  #start again
        print ("Goodbye!")
    else: #validate selection
        validateSelection(startAgain)

def displayMenu(menuSelection, startAgain): #displays introduction and menu options
    print("")
    print("The rules are:")
    print("-Paper Covers Rock")
    print("-Rock Smashes Scissors")
    print("-Scissors Cuts Paper")
    print("")
    startProgramAgain(startAgain)

def startProgramAgain(startAgain): #restarts or quits the program
        startAgain = input("Make another selection, 'y' or 'n'? ")
        while startAgain.lower() != "y": # quits the program
            print("Goodbye!")
            break
        else:
            main() #restarts the program, going back to main module

def validateSelection(startAgain): #validates the selection, only allowing 1-3
        print("")
        print("     THAT IS NOT A VALID SELECTION, PLEASE TRY AGAIN!\n")
        startProgramAgain(startAgain)

def playWithComputer(startAgain): #Module that compares a computers random variable to your selected variable
#Decides who the winner is when a player competes against the computer

    computer1 = random.randint(1,3)
    #tesrer statement print (computer_choice)
    if computer1 == 1:
        user1 = input("Enter your choice. 1 for paper, 2 for rock, 3 for scissors: ")
        if user1 == "1":
            print ("Tie. Computer chose paper and you chose paper")
            startProgramAgain(startAgain)
        elif user1 == "2":
            print ("Lose. Computer chose paper and you chose rock")
            startProgramAgain(startAgain)
        elif user1 == "3":
            print ("Win. Computer chose paper and you chose scissors")
            startProgramAgain(startAgain)
        else:
            print ("Try again! Only choose 1, 2, or 3.")
            startProgramAgain(startAgain)
                   
    elif computer1 == 2:
        user1 = input("Enter your choice. 1 for paper, 2 for rock, 3 for scissors: ")
        if user1 == "1":
            print ("Win. Computer chose rock and you chose paper")
            startProgramAgain(startAgain)
        elif user1 == "2":
            print ("Tie. Computer chose rock and you chose rock")
            startProgramAgain(startAgain)
        elif user1 == "3":
            print ("Lose. Computer chose rock and you chose scissors")
            startProgramAgain(startAgain)
        else:
            print ("Try again! Only choose 1, 2, or 3.")
            startProgramAgain(startAgain)
            
    elif computer1 == 3:
        user1 = input("Enter your choice. 1 for paper, 2 for rock, 3 for scissors: ")
        if user1 == "1":
            print ("Lose. Computer chose scissors and you chose paper")
            startProgramAgain(startAgain)
        elif user1 == "2":
            print ("Win. Computer chose scissors and you chose rock")
            startProgramAgain(startAgain)
        elif user1 == "3":
            print ("Tie. Computer chose scissors and you chose scissors")
            startProgramAgain(startAgain)
        else:
            print ("Try again! Only choose 1, 2, or 3.")
            startProgramAgain(startAgain)

def playWithPlayer(startAgain):

    print ("")
    #Get user 1's input
    user1 = input("(Player 1) Enter your choice. 1 for paper, 2 for rock, 3 for scissors: ")
    #Get user 2's input.
    user2 = input("(Player 2) Enter your choice. 1 for paper, 2 for rock, 3 for scissors: ")
    print ("")


    #There are nine possible outcomes. 3 wins for user 1, 3 wins for user 2, and 3 ties for both users
    #First code user1 winning with paper versus user2 rock
    if (user1 == "1" and user2 == "2"):
        print ("Player 1 wins! Player 1 chose paper and Player 2 chose rock.")
    # user1 winning with rock versus user2 scissors
    elif (user1 == "2" and user2 == "3"):
        print ("Player 1 wins! Player 1 chose rock and Player 2 chose scissors.")
    # user1 winning scissors rock versus user2 paper
    elif (user1 == "3" and user2 == "1"):
        print ("Player 1 wins! Player 1 chose scissors and Player 2 chose paper.")

    #Second code user2 winning with paper versus user1 rock
    elif (user2 == "1" and user1 == "2"):
        print ("Player 1 wins! Player 1 chose paper and Player 2 chose rock.")
    # user2 winning with rock versus user1 scissors
    elif (user2 == "2" and user1 == "3"):
        print ("Player 1 wins! Player 1 chose rock and Player 2 chose scissors.")
    # user2 winning scissors rock versus user1 paper
    elif (user2 == "3" and user1 == "1"):
        print ("Player 1 wins! Player 1 chose scissors and Player 2 chose paper.")
    

    #Third code user1 tieing with paper versus user2 paper
    elif (user1 == "1" and user1 == "2"):
        print ("Tie! Player 1 chose paper and Player 2 chose paper.")
    # user2 winning with rock versus user1 scissors
    elif (user1 == "2" and user2 == "2"):
        print ("Tie! Player 1 chose rock and Player 2 chose rock.")
    # user2 winning scissors rock versus user1 paper
    elif (user1 == "3" and user1 == "3"):
        print ("Tie! Player 1 chose scissors and Player 2 chose scissors.")
    else:
        print ("Try again! Only choose 1, 2, or 3.")

    print ("")

    startProgramAgain(startAgain)

#Call the main function
main()
