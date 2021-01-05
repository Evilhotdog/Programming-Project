import random
import csv
class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0
    def round(self):
        # Round method is called for each player to make the player play 1 round
        print("Round "+str(j))
        diceroll1 = random.randint(1,6)
        diceroll2 = random.randint(1,6)
        overallroll = diceroll1+diceroll2
        print("You rolled a "+str(diceroll1)+" and a "+str(diceroll2)+". This gives you a total of "+str(overallroll)+". ")
        self.score = self.score + overallroll
        if overallroll%2==0:
            print("Roll is even. Adding 10")
            self.score = self.score + 10
        else:
            print("Roll is odd. Subtracting 5")
            self.score = self.score - 5
            if self.score <= 0:
                print("Your score dropped below 0. You lose")
                self.score = 0
                return (self)
        if diceroll1 == diceroll2:
            print("Dice are even. Roll again")
            extraroll = random.randint(1,6)
            print("You rolled a "+str(extraroll)+". Adding to score. ")
            self.score = self.score + extraroll 
        print(self.name+", your total score is now "+str(self.score)+". ")
        input("Press any key to continue")
        return 0
def endgame(loser):
    if losingPlayer:
        # if a losing player has been established by one's score hitting zero, it does not need to compare scores
        if losingPlayer == p1:
            print("p1 lost")
            return p2
        else:
            print("p2 lost")
            return p1
    else:
        # otherwise, their scores should be compared
        if p1.score > p2.score:
            print("p1 won")
            return p1
        elif p2.score > p1.score:
            print ("p2 won")
            return p2
        elif p1.score == p2.score:
            print ("equal")
            # if the scores are equal, then the winning player is dictated by extra times so that should be returned
            return(extratime())
def extratime():
    while True: # continues to play rounds of extra time until a winner is established
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        print("Player 1 rolled "+roll1+". Player 2 rolled "+roll2)
        if roll1 > roll2:
            return p1
        elif roll2 > roll1:
            return p2
def checkPassword(passwordinput):
    # the username and password lists are set up so corresponding usernames and passwords have the same index. this checks if the password with the same index as the given username matches the password given
    if passwords[usernameIndex-1] == passwordinput:
        return True
    else:
        return False
def findUsername(usernameInput):
    for i in range(len(usernames)):
        if usernameInput.lower() == usernames[i].lower():
            print("Username found")
            print("The index is "+str(i))
            return i+1
def saveToFile(winner):
    with open("leaderboard.csv","r") as leaderboard: # open leaderboard to turn into list
        leaderboardList = list(csv.reader(leaderboard))
    print (leaderboardList)
    leaderboardList.append([winner.name, str(winner.score)])
    leaderboardList = insertionsort(leaderboardList)
    leaderboardList.reverse()
    while len(leaderboardList) > 5:
        leaderboardList.pop() # removees lowest scores until 5 remain. this is a leaderboard, after all
    print(leaderboardList)
    with open("leaderboard.csv","w") as leaderboard:
        seperator = ","
        for leaderboarditem in leaderboardList:
            #print(1)
            leaderboard.write(seperator.join(leaderboarditem)+"\n")
def insertionsort(ilist):
    print("Begin sort")
    for i in range(len(ilist)):
        key =  ilist[i]
        j = i-1
        #print(ilist)
        while j >= 0 and int(key[1])  < int(ilist[j][1]):
            ilist[j+1] = (ilist[j])
            j-=1
        ilist[j+1] = key
    return ilist
usernameFound = False
usernames = ["player1","player2","player3"]
passwords = ["Admin","Password","123"]
for i in range(2):
    while True:
        usernameInput = str(input("Please enter a username"))
        usernameIndex = findUsername(usernameInput)
        if usernameIndex:
            usernameFound = True
        else:
            usernameFound = False
            print("You have not inputted a correct username. Would you like to try again or create an account?")
            while True:
                choice = str(input()).title()
                if choice == "Try Again":
                    break
                elif choice in ["Create Account", "Create An Account", "Account"]:
                    newUsername = input("What is your username?")
                    newPassword = str(input("What is your password?"))
                    usernames.append(newUsername)
                    passwords.append(newPassword)
                    break
                else:
                    print("Incorrect answer, please try again")
        if usernameFound == True: 
            while True: 
                passwordinput = str(input("Please enter your password"))
                if checkPassword(passwordinput) == True:
                    print("Access granted")
                    break
                else:
                    print("Incorrect password")
            break
    if i == 0:
        p1 = Player(usernameInput)
    else:
        p2 = Player(usernameInput)
losingPlayer = 0
for i in range(5):
    # reset scores to mark new game
    p1.score = 0
    p2.score = 0
    for j in range(1,6):
        cont = p1.round() # return value of round method is a losing player, or 0 to mark no players having reached a score of 0
        if cont != 0:
            losingPlayer = cont
            break
        cont = p2.round()
        if cont != 0:
            losingPlayer = cont
            break
    print("End of game")
    winningPlayer = endgame(losingPlayer)
    print("The winner is "+winningPlayer.name)
    saveToFile(winningPlayer)
