
class Team(object):
    list = []
    Won = 0
    Lost = 0
    Tie = 0
    Goals = 0

    def __init__(self,name):
        self.name = name

    def WinOrLose(self,In,Goal):
        if In == 1:
            self.Won = self.Won + 1
        elif In == 0:
            self.Tie = self.Tie + 1
        else:
            self.Lost = self.Lost + 1

        self.Goals += Goal

    def ToString(self):
        print("Name: " + self.name)
        print("Wins: " + str(self.Won) + " Losses: " + str(self.Lost) + " Ties: " + str(self.Tie))
        print("Goals: " + str(self.Goals))

        

    

    

