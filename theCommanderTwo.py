
class profile:
    def __init__(self, name, password):
        self.name = name 
        self.password = password
    
    def getName(self):
        return self.name

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


def createProfile():
    print("Enter your player name:")
    userName = input()
    print("Choose a password")
    passWord = input()
    userProfile = profile(userName,passWord)
    print("Hello " + userProfile.getName())
    



    
    
    



createProfile() 