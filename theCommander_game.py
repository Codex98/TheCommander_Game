#GOALS
#want to make a SET and rememberable inventory that you can add too from perhaps a cache of money using money 
#in this set inventory, the user can choose how much of the inventory he wants to use 
# maybe set limits? like the wildcat always looses to the zero, unless steve is flying it 
# want it to be as variable as possible so it doesnt get boring- some sort of a randomosity generator (what are those called?)
# can we make the theater of war vary per restart of the code??? 
 # make it recall the profile that we made earlier. also, place the profile within the code using pickling 

print(" * * * THE COMMANDER * * * ")

print("A MILITARY TACTIC GAME")

print("press any key to continue!")

print("")


userChoice = " "


while(userChoice != "Q"):

    userChoice = input()

    if (userChoice != "Q"):

        print("Welcome to this game!")
        print("choose one option:")
        print("enter S to start")
        print("enter P to view your profile")
        print("don't have a profile? make one now by pressing M!")
        print("enter Q to quit")
        print("enter M to make a profile, or change your profile") # how can the user get into the profile which is stored and change it? 

                     # also make it save the profile, using pickling and object orientation 
        if(userChoice.upper().strip() == "S"):
            print("YOU are Colonel" + ". YOU are the commander of Task Group 67, fighting the Nazis in Europe")           
            print("are you ready? enter Y/N, or Q to quit")
        elif userChoice == "Y": 
                print("Good Luck, Colonel" + "!") #make this recall the profile name 
                print("Alright.")
                print("We've got a situation, colonel")
                print("The Nazi's have dug in at the Ardennes. ground forces are having a hard time routing them out...")
                print("we need you to send in a strike!")
                print("you've got three options:")
                print("either choose 1) high altitude bombers- not vulnerable to flak, but not really accurate")
                print("2) low altitude inline engine fighters- accurate, but very vulnerable to ground fire")
                print("... or 3), low altitude radial engine fighters- expensive but safe for your crews")
                if userChoice == "1": 
                    print("bombers away! do you want to send an escort? if you dont, they could be shot down!")
                    print("type AFFIRMATIVE or NEGATIVE to decide")
                    if userChoice == "AFFIRMATIVE":
                        print("good! escort has intercepted an enemy effort to shoot down your bombers, and they've been saved!")
                    elif userChoice == "NEGATIVE": 
                            print("OH NO! some of your bombers were shot down. its sort of okay, though, becuase a few got over the target to drop the bombs!")
                    input("type 'what happened' to see the results of the raid")
                    if userChoice == "what happened":
                        print("your bombers got over the target, and 50% of the german force has been knocked out!")
                        print("good job!") 
                                    #print("if you want to continue the game, press C, or if you want to quit, Q is always an option")
                                    #then if userchoice C, we'd take the code back to the beginning of the game; if userchoice is equal to Q, break the loop
                                    #also do this below... do an else which goes back to C... or make seeing the results mandatory?? 
                elif userChoice == "2":
                    print("fighters away! do you want to send an escort? if you dont, they could be jumped and have to drop bombs before they get to the target!")
                    input("type 'yes', or 'no' to decide:")
                    if userChoice == "yes":
                            print("cool! the fighters are on their way!")
                    elif userChoice == "no":
                        print("not a big deal- these are fighters, after all")
                        input("type 'what happened' to see the results of the raid")
                        if userChoice == "what happened":
                            print("Awesome! your fighters got over the target- a few of them were shot down, but almost all the Nazi force was destroyed! good job!")
                    elif userChoice == "3": 
                        print("fighters away! do you want to send an escort? if you dont, they could be jumped and have to drop bombs before they get to the target!")
                        input("type 'yes', or 'no' to decide:")
                        if userChoice == "yes":
                                print("yikes- thats kind of expensive")
                        elif userChoice == "no":
                                print("its all good- these are fighters, after all")
                        input("print 'what happened' to see the results of the raid")
                        if userChoice == 'what happened': 
                                print("you're fighters succesfully destroyed 100% of the Nazi force!! tremendous job!")
        elif userChoice == "N": 
                print("Do you want to quit? answer YEP/NO")
        elif userChoice == "YEP": #make this break the loop 
                print("goodbye!!")
        elif userChoice == "NO": 
                    print("let's continue!")
        elif(userChoice.upper().strip() == "P"):
             print("Here's your profile!")
             print("profile:")
        elif(userChoice.upper().strip() == "M"):
            print("What's your name?")
            input()
            print(userChoice)
            print("you are a colone!")
        elif(userChoice.upper().strip() == "Q"):
            print("goodbye!!! ")

