import random

def Posture():
 posture=random.choice(["sitting","standing"])
 print(f"Are you sitting, Nexus?{posture}")
 if(posture=="sitting"):
    print("Stand up.")
    return "sitting"
 else:
     print("Can check the direction.") 
     return "standing" 

def CorrectDirection():
    direction=random.choice(["right","left","facing"])
    print(f"Are you facing the door, Nexus?{direction}")
    while(direction!="facing"):

        print(f"Is the door on your right?{direction}")
        if(direction=="right"):
            print("Trun right, Nexus.")
            direction="facing"
        else:  
           print(f"Is the door on your left?{direction}")
           if(direction=="left"):
            print("Trun left, Nexus.")
            direction="facing"
        print(f"Are you facing the door, Nexus?{direction}")   
    print("Can walk toward the door.")         
            
def Distance():
    steps=[1,2,3,4,5,6,9,10] 
    distance=random.choice(steps) #distance tells how many steps are remaining
    while(distance>0):
        if(distance==1): #to be print a corrected grammarly sentence
            print(f"Moving..{distance} step is remaining.")
            distance=distance-1
        else:
          print(f"Moving..{distance} steps are remaining.")
          distance=distance-1
    print("0 step is remaining.")      
    print("Open the door.")    

# the main program
#cheking posture
if(Posture()=="standing"):
    #Check the direction and correct
    CorrectDirection()
    #Check the distance then walk
    Distance()