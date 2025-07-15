import random

def guesser():
    randNum = random.randint(1,100) #Generates a random number between 1 and 100
    count = 0
    while True:                                                    #Runs the code till the loop breaks
        try:
            i=int(input("Guess the number between 1 and 100: "))
            if i != randNum:                                        #Checking if the user input is not equal to randNum
                diff = i-randNum
                if diff>20:
                    print('Guess was too high, try again')
                elif diff<-20:
                    print('Guess was too low, try again')
                count += 1
            else:
                plural = 'ies' if count != 1 else 'y'              #Setting the plural values to 'ies' or 'y' to mention it while printing
                print(f'Congratulations your guess is correct, you took {count} tr{plural}')
                break
        except ValueError:                           #This Except block runs when ValueError occurs
            print('Please input only integers')


guesser()
