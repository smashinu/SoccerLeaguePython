import teams
import random

class GamesToPlay(object):
    TeamOneGoals = 0
    TeamTwoGoals = 0

    def __init__(self,TeamOne,TeamTwo,Tempreture):
        self.TeamOne = TeamOne
        self.TeamTwo = TeamTwo
        self.Tempreture = Tempreture
        self.PlayGame()

    def PlayGame(self):
        
        if self.Tempreture > 40:
            TeamOneGoals = random.randint(0,4)
            TeamTwoGoals = random.randint(0,4)
        elif self.Tempreture > 30:
            TeamOneGoals = random.randint(0,3)
            TeamTwoGoals = random.randint(0,3)
        else:
            TeamOneGoals = random.randint(0,2)
            TeamTwoGoals = random.randint(0,2)

        self.TeamOneGoals = TeamOneGoals
        self.TeamTwoGoals = TeamTwoGoals

        if TeamOneGoals == TeamTwoGoals:
            self.TeamOne.WinOrLose(0,TeamOneGoals)
            self.TeamTwo.WinOrLose(0,TeamTwoGoals)
        elif TeamOneGoals > TeamTwoGoals:
            self.TeamOne.WinOrLose(1,TeamOneGoals)
            self.TeamTwo.WinOrLose(-1,TeamTwoGoals)
        else:
            self.TeamOne.WinOrLose(-1,TeamOneGoals)
            self.TeamTwo.WinOrLose(1,TeamTwoGoals)
        

    def ToString(self):
        print("Tempreture: " + str(self.Tempreture))
        print("Team One:" + self.TeamOne.name +" Goals: " + str(self.TeamOneGoals))
        print("Team two: " + self.TeamTwo.name + " Goals: " + str(self.TeamTwoGoals))
   
