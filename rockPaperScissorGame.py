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
    playerRoundWins += 1
    print("You won this round!")

#resultOfComputerWin() ändrar datorns antal vinster och presenterar vinnare
def resultOfComputerWin():
    computerRoundWins +=1
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
            resultOfPlayerWin
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
            

#oneRound() ska kontrollera en "sten sax påse" runda
def oneRound():
    playerChoice = input("Pick your move by choosing a number:\n1. Rock\n2. Paper\nScissor")
    computerChoice = random.randrange(1,4)
    calculateWinner(int(playerChoice),computerChoice)

#main() ska introducera spelet och hålla en loop för flera rundor
def main():

    #while-loop som körs tills spelaren inte längre vill spela
    wantsToPlay = True
    while(wantsToPlay):
        print("Welcome to rock, paper, scissor! You'll be playing one round.\nYou'll be playing against the computer.")
        print("-"*20)
        #while-loop som körs tills någon vunnit "bäst av..."
        noWinnerYet = True
        while(noWinnerYet):
            #Anropar en runde per loop
            oneRound()
            noWinnerYet = False #Än så länge bara en runda
        playerRoundWins = 0
        playerRoundWins = 0
        #Uppdatera statsen på matcher vunna
    

main()