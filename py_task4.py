import random
import string

digits=['0','1','2','3','4','5','6','7','8','9']
up_cases=list(string.ascii_uppercase)
low_cases=list(string.ascii_lowercase)
symbols=['~','!','@','#','$','%','^','&','*','_']
Allowed_characters=digits+up_cases+low_cases+symbols

#Offering the two options to user to choose from
user_choice=input("Would you create a password using \"Random Password Generator\" or \"Password Strength Checker\"?")
#================Random Password Generator=================#
if(user_choice=="Random Password Generator"):
   pass_len=int(input("Determine the length of your password. (Minimum 8 characters)"))
   if(pass_len >=8):
        password=[]
        password=random.choices(Allowed_characters,k=pass_len) #fills the list by number pass_len of random elements
        print(f'Your password is :  {"".join(password)}')   
   else:
        print("Minimum 8 charcters")

#================Password Strength Checker=================#
elif(user_choice=="Password Strength Checker"):
    password=input("Enter your password.(Minimum 8 characters)")
   if(len(password)>=8):
#----------------weakScenario---------------------------------       
           
   else:
        print("Minimum 8 charcters")



