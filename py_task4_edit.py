import random
import string
#========================================
digits=['0','1','2','3','4','5','6','7','8','9']
up_cases=list(string.ascii_uppercase)
low_cases=list(string.ascii_lowercase)
symbols=['~','!','@','#','$','%','^','&','*','_']
Allowed_characters=digits+up_cases+low_cases+symbols
#---------passwords strength Assessment ----------------#
def pass_stren(pas):
   count_digits=count_up=count_low=count_symbols=0
   #-----------------counting char and classifying--------------------
   for char in pas :
        if(char in digits):
                  count_digits=count_digits+1
        if(char in up_cases):
                  count_up=count_up+1
        if(char in low_cases): 
                  count_low=count_low+1
        if(char in symbols):
                  count_symbols = count_symbols +1
   counters=[count_digits,count_up, count_low,count_symbols]
    #----------------strength Assessment---------------------------------
   if(counters.count(0)==3):
        return'W'
   elif(counters.count(0)==2): 
        return'M'
   elif(counters.count(0)==1):
        return'S'               
   elif(counters.count(0)==0):
        return'VS'                     
#----------Offering the two options to user to choose from----------------
while(True):
  user_choice=input("Would you create a password using \"Random Password Generator\" or \"Password Strength Checker\"?")
#================Random Password Generator=================#
  if(user_choice=="Random Password Generator"):
     pass_len=int(input("Determine the length of your password. (Minimum 8 characters)"))
     if(pass_len >=8):
          password=[]
          password=random.choices(Allowed_characters,k=pass_len) #fills the list by number pass_len of random elements
          while(pass_stren(password)=='M' or pass_stren(password)=='W'):
           password=random.choices(Allowed_characters,k=pass_len) #password is regenerated if medium or weak, unless it is strong or very strong.         
          print(f'Your password is :  {"".join(password)}')
          confirmed=input("Would you like to confirm this password? (y/n)")
          if(confirmed=='y'):#If yes, will end the program. If no, will ask again about the way to create the password.
            break                 
     else:
          print("Minimum 8 charcters")
#================Password Strength Checker=================#
  count_digits=count_up=count_low=count_symbols=0
  if(user_choice=="Password Strength Checker"):
      password=input("Enter your password.(Minimum 8 characters)")   
      if(len(password)<8):
           print("Minimum 8 charcters")
      elif(len(password)>=8):   
#----------------password Strength assessment---------------------------------
          if(pass_stren(password)=='W'):
                 print("Weak password")#after getting weak password, it will ask again for the way to create the password.
          elif(pass_stren(password)=='M'): 
                 print("Medium password") #after getting medium password, it will ask again for the way to create the password.
          elif(pass_stren(password)=='S'):
                 print("strong password")
                 confirmed=input("Would you like to confirm this password? (y/n)")
                 if(confirmed=='y'):#If yes, will end the program. If no, will ask again about the way to create the password.
                  break                  
          elif(pass_stren(password)=='VS'):
                 print("Very strong password")                     
                 confirmed=input("Would you like to confirm this password? (y/n)")
                 if(confirmed=='y'):#If yes, will end the program. If no, will ask again about the way to create the password.
                  break                      