playerWins = 0
computerWins = 0

playerRoundWins = 0
computerRoundWins = 0

#Ska finnas globala variabler för vunna rundor och för matcher vunna för både datorn och spelaren

#resultOfDraw() skriver ut vad som händer vid oavgjort

#resultOfPlayerWin() ändrar spelarens antal vinster och presenterar vinnare

#resultOfComputerWin() ändrar datorns antal vinster och presenterar vinnare

#calculateWinner() genom if-satser kolla vem som vinner
    #if för att se om användaren valt 1, jämför sten mot användarens val
        #if för varje möjlig val datorn kan göra
    #if för att se om användaren valt 1, jämför sax mot användarens val
        #if för varje möjlig val datorn kan göra
    #if för att se om användaren valt 1, jämför sax mot användarens val
        #if för varje möjlig val datorn kan göra
            

#oneRound() ska kontrollera en "sten sax påse" runda
    #Användarens val tas av input ich datorns av slump, sedan räknas vinnaren ut med calculateWinner()

#main() ska introducera spelet och hålla en loop för flera rundor
    #while-loop som körs tills spelaren inte längre vill spela
        #while-loop som körs tills någon vunnit "bäst av..."
            #Anropar en runde per loop
        #När ute ur inre loopen, nollställ vunna rundor
        #Uppdatera statsen på matcher vunna