import random

#Ska finnas globala variabler för vunna rundor och för matcher vunna för både datorn och spelaren
playerWins = 0
computerWins = 0

playerRoundWins = 0
computerRoundWins = 0

#resultOfDraw() skriver ut vad som händer vid oavgjort
def resultOfDraw():
    print("It resultet in a draw")

#resultOfPlayerWin() ändrar spelarens antal vinster och presenterar vinnare
def resultOfPlayerWin():
    global playerRoundWins
    playerRoundWins =+ playerRoundWins + 1
    print("You won this round!")

#resultOfComputerWin() ändrar datorns antal vinster och presenterar vinnare
def resultOfComputerWin():
    global computerRoundWins
    computerRoundWins = computerRoundWins + 1
    print("The computer won")

#calculateWinner() genom if-satser kolla vem som vinner
def calculateWinner(playerChoice, computerChoice):
    #if för att se om användaren valt 1, jämför sten mot användarens val
    if(playerChoice==1):
        #if för varje möjlig val datorn kan göra
        if(computerChoice==1):
            resultOfDraw()
        elif(computerChoice==2):
            resultOfComputerWin()
        else:
            resultOfPlayerWin()
    #elif för att se om användaren valt 2, jämför sax mot användarens val
    elif(playerChoice==2):
        #if för varje möjlig val datorn kan göra
        if(computerChoice==1):
            resultOfPlayerWin()
        elif(computerChoice==2):
            resultOfDraw()
        else:
            resultOfComputerWin()
    #else för att se om användaren valt 3, jämför sax mot användarens val
    else:
        #if för varje möjlig val datorn kan göra
        if(computerChoice==1):
            resultOfComputerWin()
        elif(computerChoice==2):
            resultOfPlayerWin()
        else:
            resultOfDraw()
            
#function that handles if-statement to deliver the news of the computers choice
def computerChoiceInformation(computerChoiceNum):
    if(computerChoiceNum==1):
        print("The computer choosed rock")
    elif(computerChoiceNum==2):
        print("The computer choosed paper")
    else:
        print("The computer choosed scissor")

#oneRound() ska kontrollera en "sten sax påse" runda
def oneRound():
    playerChoice = input("Pick your move by choosing a number:\n1. Rock\n2. Paper\n3. Scissor\nEnter choice: ")
    computerChoice = random.randrange(1,4)
    computerChoiceInformation(computerChoice)
    calculateWinner(int(playerChoice),computerChoice)
    print(f"Player has:   {playerRoundWins} rounds")
    print(f"Computer has: {computerRoundWins} rounds")
    print("-"*20)

#wantsToPlatAgain() checks and returns wether the player wants to play again
def wantsToPlayAgain():
    answer = int(input("Do you want to play again?\n1.Yes\n2.No\nEnter number for answer: "))
    if(answer==1):
        return True
    else:
        return False


#main() ska introducera spelet och hålla en loop för flera rundor
def main():
    #Definierar globala variabler för main()
    global playerWins
    global computerWins
    global playerRoundWins
    global computerRoundWins

    #while-loop som körs tills spelaren inte längre vill spela
    wantsToPlay = True
    while(wantsToPlay):
        rounds = int(input("How many rounds do you want to play \"best of\" for? It has to be an uneven number!\nEnter amount of rounds: "))
        neededRoundsToWin = int((rounds+1)/2)
        print("-"*20)
        print(f"Welcome to rock, paper, scissor! You'll be playing {neededRoundsToWin} rounds.\nYou'll be playing against the computer.")
        print("-"*20)
        #while-loop som körs tills någon vunnit "bäst av..."
        while(playerRoundWins!=neededRoundsToWin and computerRoundWins!=neededRoundsToWin):
            #Anropar en runde per loop
            oneRound()
        if(playerRoundWins>computerRoundWins):
            playerWins = playerWins+1
            print("You won!")
        else:
            computerWins = computerWins+1
            print("The computer won :(")
        playerRoundWins = 0
        computerRoundWins = 0
        wantsToPlay = wantsToPlayAgain()
        #Uppdatera statsen på matcher vunna
    print(f"After all your games, the result is:\nYour score is {playerWins}\nThe computers score is {computerWins}")

main()