
class profile:
    def __init__(self, name, password):
        self.name = name 
        self.password = password
    
    def getName(self):
        return self.name

    def setPassword(self, oldPassword, newPassword):
        if (oldPassword == self.password):
            self.password = newPassword
            return 0 
        else:
            return -1 

# # # # # # # # # # # # # # # # # # # # # # # # # # #
def printMenu():
    print("Welcome to this game!")
    print("choose one option:")
    print("enter S to start")
    print("enter L for log in")
    print("enter P to view your profile")
    print("don't have a profile? make one now by pressing M!")
    print("enter Q to quit")
# # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # #


# # # # # # # # # # # # # # # # # # # # # # # # # # #

def createProfile(name, passwird):
    newProfile = profile(name, passwird)
    return newProfile
    
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
#MAIN PROGRAM 
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # #

#call the printMenu function and he'll get to work. 
printMenu()


# main menu functionality 
userChoice = ""
userProfile = None

while(userChoice!="Q"):
    userChoice = input("\t-->>")
    #User chose to start the / a  Game...
    if(userChoice == "S"):
        if(userProfile!=None):
            print("Hello, " + userProfile.getName() + "!")
        else:
            print("You must login or signup to show that")
    #user wnats to log in 
    elif(userChoice=="L"):
        pass 
    #show profile 
    elif(userChoice=="P"):
        pass
    # create a profile 
    elif(userChoice == "M"):
        # 1) notify
        # 2) ask for name 
        # 3) ask for passwrod
        # 4) pass to the create function... 
        print("CREATE A PASSWORD")
        print("Enter your player name:")
        userName = input()
        print("Choose a password")
        passWord = input()
        userProfile = createProfile(userName,passWord)
    #lets go. nothing here for now... 
    elif(userChoice == "Q"):
        pass 