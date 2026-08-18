#-------**-------**---------**------Number Guessing Game-------**-------**---------**------#
import random
#----variables----
rounds_played,rounds_won,remaining_attempts,succ_attempts,finale_score,multiplier=0,0,0,0,0,1
answer=''
print("Welcome Player.")
#-------------------------The round loop-----------------------------------#
while(answer=='y' or rounds_played==0):
    rounds_played=rounds_played+1
    #------------------start of the round----------------------#
    score=0
    multiplier=1
    secret=random.randint(1,100)
    print("I'm thinking of a number between 1 and 100.")
    print("You have 6 attempts to guess it.")
    #-------------------------Attempts Loop---------------------------#
    remaining_attempts=6
    while(remaining_attempts>0):
      remaining_attempts= (remaining_attempts)-1
      print(f"Attempt {6-(remaining_attempts)}/6")
      guess=int(input("Enter your guess: "))
      #----------------Failed guess(attempt)-------------------#
      if(guess!=secret):
         #
        if(guess<(secret/2)):
           print("Too low. Guess a higher number.")
        elif((secret/2)<=guess<secret):
           print("Lower. Guess a higher number.")   
        elif(secret<guess<=(secret*(3/2))):
           print("Higher. Guess a lower number.")
        elif(guess>(secret*(3/2))):
           print("Too high. Guess a lower number.")                  
    #_____successful guess(attempt)-----#
      else: 
            print("Congratulations!") 
            print("You guessed the number correctly.")
            multiplier=1+remaining_attempts
            score=multiplier 
            rounds_won=rounds_won+1
            break      
   #---------------at the end of the round =After 6 attepts or less-------------------------
    if(score==0):
       print(f"The secret number is : {secret}")  
    finale_score=finale_score+score
    print(f"Rounds won : {rounds_won}")
    print(f"Multipliers : {multiplier}")
    print(f"Points earned : {score}")#score of each round
    answer=input("Do you want to play another round? (y/n)")#The last line in the program begore ending the round loop    
print(f"Total rounds played : {rounds_played}")
print(f"Rounds won : {rounds_won}")
print(f"Final Score : {finale_score}")#The accumulated score