import random


def guesser():
    randNum = random.randint(1,100)
    count = 0
    while True:
        try:
            i=int(input("Guess the number between 1 and 100: "))
            if i != randNum:
                diff = i-randNum
                if diff>20:
                    print('Guess was too high, try again')
                elif diff<-20:
                    print('Guess was too low, try again')
                count += 1
            else:
                plural = 'ies' if count != 1 else 'y'
                print(f'Congratulations your guess is correct, you took {count} tr{plural}')
                break
        except TypeError and ValueError:
            print('Please input only integers')


guesser()
