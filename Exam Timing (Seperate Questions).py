#COPY AND PASTE THIS CODE INTO A NEW FILE


#Exam Timing (Seperate Questions)
#Q = Question
import time
import sys
#Subroutine to time exam questions
def countdown(QAmount):
    #This procedure runs the function of displaying a countdown
    
    while QAmount > 0:
        #Loops code until there are no questions left
        
        for i in range(0, QAmount):
            QAmount = QAmount - 1
            QTime = int(input("Enter the number of marks for question {}/ The amount of time you need for question {} (at least 1 min)\n".format(i+1, i+1)))
            Time = QTime * 60
            #Converts the input time into seconds
            
            start = input("To start the timer, press enter. To quit, type 'q':\n")
            #Allows the user to be prepared before the timer for each question begins
            
            if start == "":
                if Time == 60:
                    print(QTime, "min")
                else:    
                    print(QTime, "mins")
                """These if and else statements output 'min' if the time is a
                    singular minute, and 'mins' if the time is plural"""
                while Time > 0:
                    #Loops until the Time (in seconds) hits zero
                    mins, secs = divmod(Time, 60)
                    #divmod returns a quotient and a remainder (when the two inputs are integers)
                    #quotient = The result of dividing two numbers
                    
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    #'{;02d}', '02' displays a number in a two-digit form "00"
                    #The letter 'd' displays a number in decimal form
                    
                    print(timer, end="\r \n")
                    #The letter \r shifts your mouse cursor back to the beginning of a string/line
                    #In this case, the cursor shifts to a new line
                    
                    time.sleep(1)
                    #Waits one second before starting the countdown
                    
                    Time -= 1
                    #The code under this while loop displays the countdown to the user
                
            elif start == "q" or start == "Q" or start != "":
                print("Goodbye :)")
                sys.exit()
                #Stops running the program
                   
    print("\nYOU HAVE REACHED THE END OF THE PAPER\n")
                
# Main Program
# Allows the user to Input the Number of Questions required to be answered
print("""'Question Countdown'

PLEASE READ!

This tool allows you to enter the number of exam questions in a paper,
and the amount of marks needed for each question (1 min per mark).

You may require more time to complete a question than that stated by the
number of marks, which is why this program allows you to enter the amount
of time you believe is needed.

This timer can only be used for completing one question at a time. Complete
one question, then after the time for one question has reached 0:00,
mark the question, write down the total score for that question, then,
write down the time needed to complete the next question.

Repeat this process until you've reached the end of the paper.

EACH QUESTION MUST BE AT LEAST 1 MIN LONG

BEGIN\n""")
      
QAmount = int(input("Enter the number of questions in the exam:\n"))
# Function call
while QAmount > 0:
    countdown(int(QAmount))
