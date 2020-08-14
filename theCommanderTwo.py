import pickle 
TRED =  '\033[31m' # Green Text
TWHITE = '\033[37m'
class profile:
    def __init__(self, name, password):
        self.name = name 
        self.password = password
    
    def getName(self):
        return self.name
    
    def isPassword(self, attmpt):
        if(attmpt == self.password):
            return True
        else:
            return False
    
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
# need to make this uncallable if logged in.... 
# also need to figure out how to make multiple log ins eventaully?? 
def createProfile(name, passwird):
    newProfile = profile(name, passwird)
    #pickle the profile....
    with open('profile_data', 'wb') as output:
        pickle.dump(newProfile, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(newProfile, output, pickle.HIGHEST_PROTOCOL)
    return newProfile


def login():
    profileThere = False
    try:
        with open('profile_data','rb') as readIn:
            validProfile = pickle.load(readIn)
            profileThere = True
    except:
        print(TRED + "FILE ERROR", TWHITE)
    if(profileThere):
        fail = True
        while(fail):
            print("LOG IN:")
            print("____________________________")
            name = input("USERNAME -->>").strip()
            password= input("\t PASSWORD -->>").strip()
            if(name == validProfile.getName() and validProfile.isPassword(password)):
                fail = False
                return validProfile
            else:
                print (TRED + "UserName and or Password do not match!" , TWHITE)
    readIn.close()
  
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
        userProfile = login()
        print("Welcome, " + userProfile.getName() + "!")
        pass 
    #show profile 
    elif(userChoice=="P"):
    # create a profile 
    elif(userChoice == "M"):
        # 1) notify
        # 2) ask for name 
        # 3) ask for passwrod
        # 4) pass to the create function... 
        if(userProfile == None):
            print("CREATE A PASSWORD")
            print("Enter your player name:")
            userName = input().strip()
            print("Choose a password")
            passWord = input().strip()
            userProfile = createProfile(userName,passWord)
    #lets go. nothing here for now... 
    elif(userChoice == "Q"):
        pass 