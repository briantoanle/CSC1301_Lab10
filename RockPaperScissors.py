import random

ROCK=1
PAPER=2
SCISSOR=3

choice = [' chose rock',' chose paper',' chose scissors']
result = ['Congratulations you win!','The match was a tie','Computer won','Goodbye']
def RockPaperScissors():
    print("The Rock Paper Scissors Game")
    userInput = 0

    while userInput != -1:
        computerChoice = random.randint(1, 3)
        userInput = int(input('Enter 1 to choose rock, 2 to choose paper, '
                              '\n3 to choose scissors or -1 to quit: '))

        if userInput == -1:
            print(result[userInput])
        else:
            print('You' + choice[userInput-1])
            print('The computer'+ choice[computerChoice-1])
            if computerChoice == userInput:
                print(result[1])

            # rock 1 | paper 2 |scissor 3
            #  1 > 3
            #  3 > 2
            #  2 > 1
            elif userInput == 1 and computerChoice == 3 or userInput==3 and computerChoice==2\
                or userInput ==2 and computerChoice ==1:
                print(result[0])
            else:
                print(result[2])
#RockPaperScissors()

def exact_change(coins):
    if coins ==  0:
        print('no change')
    else:
        coins = coins / 100
        # get amount of quarters
        quarters = int(coins / .25)
        # get remainder after subtracting quarters and round it because I was getting long numbers
        quarter_new = round(coins - quarters * .25, 2)

        # get amount of dimes
        dimes = int(quarter_new / .10)
        # get remainder after subtracting dimes and also round it
        dime_new = round(quarter_new - dimes * .10, 2)

        # get amount of nickels
        nickels = int(dime_new / .05)
        # get remainder after subtracting nickels and round it
        nickel_new = round(dime_new - nickels * .05, 2)

        # get amount pennies
        pennies = int(nickel_new / .01)

    return pennies,nickels,dimes,quarters
    print(pennies,'penny')
    print(dimes,'dime')
    print(quarters,'quarters')

def testExactChange():
    input_val = int(input('Input amount in cents: '))
    pennies, nickels, dimes, quarters = exact_change(input_val)
    plural = ['pennies', 'nickels', 'dimes', 'quarters']
    if pennies <= 1:
        plural[0] = 'penny'
    if nickels <= 1:
        plural[1] = 'nickel'
    if dimes <= 1:
        plural[2] = 'dime'
    if quarters <= 1:
        plural[3] = 'quarter'

    if pennies > 0:
        print(pennies, plural[0])
    if nickels > 0:
        print(nickels, plural[1])
    if dimes > 0:
        print(dimes, plural[2])
    if quarters > 0:
        print(quarters, plural[3])
def main():
    # uncomment to test each function
    #RockPaperScissors()
    #testExactChange()
    testSwapValue()



def testSwapValue():
    i1 = int(input('Input first number: '))
    i2 = int(input('Input second number: '))
    i3 = int(input('Input third number: '))
    i4 = int(input('Input fourth number: '))
    swap_value(i1,i2,i3,i4)

def swap_value(in1,in2,in3,in4):
    in1t = in1
    in2t = in2
    in3t = in3
    in4t = in4
    in1 = in2t
    in2 = in1t
    in3 = in4t
    in4 = in3t
    print(in1,in2,in3,in4)


main()