# If you use time.sleep(seconds) if you want it to delay before doing the next line of code using the time module
import time
import random
# This is an example of data abstraction since you can use this list over and over without ever touching it again using the random module, for loops, or by specific indices


list_of_robot_moves = ['rock', 'paper', 'scissors']


def robot_turn():
    #print("I'm choosing my move")
    #time.sleep(1)
    #print("thinking...")
    #time.sleep(1)
   # print("...thinking some more...")
   # time.sleep(1)
   # print("...almost done thinking")
    robot_move = random.choice(list_of_robot_moves)
    #time.sleep(2)
    robot_move = robot_move.upper()
    return robot_move

##def again():
    #print("That's the end of your rounds.")

     
def game2():
    global uscore
    global rscore 
    uscore = 0
    rscore = 0
    if player_move == "ROCK":
        if robotsmove == "PAPER":
            print("The Robot WINS this round!!!")
            rscore += 1
            print("The Robot's score round: " + str(rscore))
        elif robotsmove == "SICCORS":
            print("You WIN this round!!!")
            uscore = uscore + 1
            print("Your score round: " + str(uscore))
        else:
            print("No one won this round.")
            print("The Robot's score round: " + str(rscore))
            print("Your score round: " + str(uscore))

    elif player_move == "SCISSORS":
        if robotsmove == "ROCK":
            print("The Robot WINS this round!!!")
            rscore = rscore + 1
        elif robotsmove == "PAPER":
            print("You WIN this round!!!")
            uscore = uscore + 1
        else:
            print("No one won this round.")
    elif player_move == "PAPER":
        if robotsmove == "SCISSORS":
            print("The Robot WINS this round!!!")
            rscore = rscore + 1
        elif robotsmove == "ROCK":
            print("You WIN this round!!!")
            uscore = uscore + 1
        else:
            print("No one won this round.")

    else:
        print("INVALID ENTRY! You lost this round.")
        rscore = rscore + 1
        print("The Robot's score round: " + str(rscore))
        print("Your score round: " + str(uscore))


# Control Panal>
def control_panal(round):
    global player_move
    global robotsmove
    count = 1
    while round >= count:
        print("Round #" + str(count) + ":")
        print("It's your turn —>")
        player_move = (
            input("Enter your move of either 'rock', 'paper', or 'scissors': \n "))
        player_move = player_move.upper()
        robotsmove = robot_turn()
        print("The Robot's move: " + (robotsmove))
        game2()
        count += 1
      
        # This compares the players selection to the robots selection and gives results accordingly
        # let me show you the problem here. you see that space in the middle?
        pass
    else:
        cont =str(input("Do you want to continue? 'Yes' or 'No' "))
        if cont.lower() == "yes":
            print("Next Round")
            round += 1
            game2()
            pass
            #print(uscore)
            #print(rscore)
        else:
            print("Goodbye!")
            round -= 2
            #print(uscore)
            #print(rscore)
        pass
        
    # This calls the again function
control_panal(int(input("How many rounds do you want to play? ")))
    # By making game have a parameter, when you call it, you can actual call another function as its argument to save a few steps in the game function
