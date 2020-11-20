import teams
import Games
import random

GameList = []

TeamOne = teams.Team("The Black Panthers")
TeamTwo = teams.Team("Iron Man")
TeamThree = teams.Team("The Mighty Ducks")
TeamFour = teams.Team("The simpsons")

SeasonOver = False
ItsToCold = 0

while SeasonOver == False:
   
    CorretInput = False

    while CorretInput == False:

        Tempreture = input("What is the tempreture today: ")
        try:
            Tempreture = int(Tempreture)
            CorretInput = True
        except:
            print("You did not enter a integer, please re-enter...")

    if Tempreture >= 15:
        
        WhoIsTeamOnePlaying = random.randint(2,4)
        if WhoIsTeamOnePlaying == 2:
            GameOne = Games.GamesToPlay(TeamOne,TeamTwo,Tempreture)
            GameTwo = Games.GamesToPlay(TeamThree,TeamFour,Tempreture) 
            GameList.append(GameOne)
            GameList.append(GameTwo)
        elif WhoIsTeamOnePlaying == 3:
            GameOne = Games.GamesToPlay(TeamOne,TeamThree,Tempreture) 
            GameTwo = Games.GamesToPlay(TeamTwo,TeamFour,Tempreture)
            GameList.append(GameOne)
            GameList.append(GameTwo)
        else:
            GameOne = Games.GamesToPlay(TeamOne,TeamFour,Tempreture)
            GameTwo = Games.GamesToPlay(TeamThree,TeamTwo,Tempreture)
            GameList.append(GameOne)
            GameList.append(GameTwo)

        print("Teams played a game...")

    else:
        ItsToCold = ItsToCold + 1
    
    if ItsToCold == 3:
        SeasonOver = True

print("Season is over, it's too cold to play...\n")

TeamOne.ToString()
TeamTwo.ToString()
TeamThree.ToString()
TeamFour.ToString()
print("\n")

counter = 1
Averagetemp = 0
HottestTemp = 0
for i in GameList:
    print("Game: " + str(counter))

    if counter % 2 == 0:
        Averagetemp += i.Tempreture

    i.ToString()
    print("\n")
    counter = counter + 1
    if HottestTemp < i.Tempreture:
        HottestTemp = i.Tempreture



Averagetemp = Averagetemp/((counter-1)/2)

print("Average tempreture: " + str(Averagetemp))
print("Hottest tempreture: " + str(HottestTemp))
