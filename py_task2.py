import time
#Taking info from user regarding tesing time
print("Enter time of testing in minutes and seconds:")
minutes=int(input("Minutes= "))
seconds=int(input("Seconds= "))
#converting to seconds
total_time = (minutes*60) + seconds #total time in seconds
#---------------------Maximum Duration-------------------------#  
if(total_time>300):
     print("Safety limit exceeded! Test duration capped to 05:00.")
     total_time=300
#-----------validation inputds---------------#
countdown=total_time
if(total_time<=0 or minutes<0 or seconds<0 or seconds>59):
        print("Invalid test duration.")  
        exit() #terminates the program immediately. 
else: 
    #countdown loop         
    while(countdown>0):
#-----------------Power State Monitoring----------------------# 
        if (total_time>30):    
            print(f"\rPOWER ON | Remaining :  {str(minutes)} : {str(seconds)}",end="")
        elif(10<total_time<=30):
            print(f"\rSTABILIZING SYSTEM | Remaining :  {str(minutes)} : {str(seconds)}",end="")
        elif(0<total_time<=10):
            print(f"\rCOOLDOWN PHASE | Do not touch | Remaining :  {str(minutes)} : {str(seconds)}",end="")                    
        countdown=countdown-1
        total_time=countdown
        minutes=total_time//60
        seconds=total_time % 60
        time.sleep(1)
#--------------------------Test Completed-----------------------------#        
    print("\r\033[KPower test completed successfully.") #overwrite the past line
  

       
    
 
 

    


    

