import random
from prettytable import PrettyTable

name = "none"
teams = ["Boston Celtics", "Milwaukee Bucks", "Chicago Bulls", "Miami Heat", "Phoenix Suns", "Golden State Warriors",
         "LA Lakers", "Dallas Mavericks"]
power = 0
oppPower = 0
draft = random.choice(teams)
yourTeam = draft
firstRoundRecord = [0, 0]
secondRoundRecord = [0, 0]
finalsRecord = [0, 0]
a = False
b = False
c = False
seasons = 0
rings = 0


class player:
    def __init__(self, ppg, apg, rpg, ):
        self.myPPG = ppg
        self.myAPG = apg
        self.myRPG = rpg

    def getPPG(self):
        return self.myPPG

    def getAPG(self):
        return self.myAPG

    def getRPG(self):
        return self.myRPG

    def increasePPG(self, p):
        self.myPPG += p

    def decreasePPG(self, o):
        self.myPPG -= o

    def increaseAPG(self, d):
        self.myPPG += d

    def decreaseAPG(self, s):
        self.myPPG -= s

    def increaseRPG(self, r):
        self.myPPG += r

    def decreaseRPG(self, e):
        self.myPPG -= e


def start():
    global name, teams, draft
    print("What is your name")
    name = input()
    print("You were selected as the first overall pick in the NBA Draft.")
    print("The", draft, "have drafted you.")
    print("You will have a great career ahead of you.")
    print("We will skip through the regular season and go straight to the playoffs. Your team, the", draft,
          ", has had a good run this season and are in the playoffs.")
    firstSeason()


def firstSeason():
    global teams, yourTeam, seasons
    print("The playoff bracket for your first season is as follows:")
    random.shuffle(teams)
    playoffTable = PrettyTable(["Seed", "Teams"])
    for i in range(len(teams)):
        playoffTable.add_row(
            [i + 1, teams[i]])
    print(playoffTable)
    y = teams.index(yourTeam) + 1
    print("Your team, the", yourTeam, "were the", y, "seed")
    print("The team that you will play against is the", 9 - y, "seeded", teams[8 - y], "in a 7 game series.")
    seasons += 1
    firstRound()


def firstRound():
    global teams, yourTeam, power, oppPower, firstRoundRecord, a
    y = teams.index(yourTeam) + 1
    if yourTeam == "Boston Celtics" or yourTeam == "Milwaukee Bucks" or yourTeam == "Golden State Warriors":
        power = 8
    elif yourTeam == "Miami Heat" or yourTeam == "Phoenix Suns":
        power = 7
    elif yourTeam == "LA Lakers" or yourTeam == "Dallas Mavericks":
        power = 6
    elif yourTeam == "Chicago Bulls":
        power = 5
    if teams[8 - y] == "Boston Celtics" or teams[8 - y] == "Milwaukee Bucks" or teams[8 - y] == "Golden State Warriors":
        oppPower = 8
    elif teams[8 - y] == "Miami Heat" or teams[8 - y] == "Phoenix Suns":
        oppPower = 7
    elif teams[8 - y] == "LA Lakers" or teams[8 - y] == "Dallas Mavericks":
        oppPower = 6
    elif teams[8 - y] == "Chicago Bulls":
        oppPower = 5
    if power - oppPower == 1 or power - oppPower == 2 or power - oppPower == 3:
        print("Your team has an advantage over the opposing team.")
    elif power - oppPower == 0:
        print("Your teams are equally matched.")
    elif power - oppPower == -1 or power - oppPower == -2 or power - oppPower == -3:
        print("The opposing team has an advantage over your team.")
    while (a == False):
        if random.randint(1, power) >= random.randint(1, oppPower):
            print("You won a game!")
            firstRoundRecord[0] += 1
            print("The record is,", firstRoundRecord[0], "-", firstRoundRecord[1])
            print("Since you won, your coach instructed you to rest up for the next game.")
        else:
            print("You lost a game.")
            firstRoundRecord[1] += 1
            print("The record is,", firstRoundRecord[0], "-", firstRoundRecord[1])
            print("Since you lost, your coach has told you to rest up or practice, its up to you.")
            print("1: Rest")
            print("2: Train")
            choice = input()
            if choice == 1:
                print(
                    "You chose to rest instead of training for the next game, hopefully this doesn't impact your gameplay.")
            elif choice == 2:
                print("You chose to go to a training session and brought your team along as well.")
                power += 1
        if firstRoundRecord[0] == 4:
            a = True
            print("You won your first round series!")
            secondRound()
        elif firstRoundRecord[1] == 4:
            a = True
            print("You lost in the first round and are now going to Cancun.")
            print("Cancun was nice, and now your gonna play another season.")
            nextSeason()


def secondRound():
    global teams, yourTeam, power, oppPower, secondRoundRecord, b
    y = teams.index(yourTeam) + 1
    matchups = [[teams[0], teams[7]], [teams[1], teams[6]], [teams[2], teams[5]], [teams[3], teams[4]]]
    for matchup in matchups:
        if yourTeam not in matchup:
            if getTeamPower(matchup[0]) < getTeamPower(matchup[1]):
                weakerTeam = matchup[0]
            else:
                weakerTeam = matchup[1]
            teams.remove(weakerTeam)
    if y == 1:
        teams.remove(matchups[0][1])
    elif y == 8:
        teams.remove(matchups[0][0])
    elif y == 2:
        teams.remove(matchups[1][1])
    elif y == 7:
        teams.remove(matchups[1][0])
    elif y == 3:
        teams.remove(matchups[2][1])
    elif y == 6:
        teams.remove(matchups[2][0])
    elif y == 4:
        teams.remove(matchups[3][1])
    elif y == 5:
        teams.remove(matchups[3][0])
    secondRoundTable = PrettyTable(["Seed", "Teams"])
    for i in range(len(teams)):
        secondRoundTable.add_row(
            [i + 1, teams[i]])
    print(secondRoundTable)
    y = teams.index(yourTeam) + 1
    print("Your team the,", yourTeam, "will play against the", teams[4-y], "in a 7 game series.")
    if yourTeam == "Boston Celtics" or yourTeam == "Milwaukee Bucks" or yourTeam == "Golden State Warriors":
        power = 8
    elif yourTeam == "Miami Heat" or yourTeam == "Phoenix Suns":
        power = 7
    elif yourTeam == "LA Lakers" or yourTeam == "Dallas Mavericks":
        power = 6
    elif yourTeam == "Chicago Bulls":
        power = 5
    if teams[4 - y] == "Boston Celtics" or teams[4 - y] == "Milwaukee Bucks" or teams[4 - y] == "Golden State Warriors":
        oppPower = 8
    elif teams[4 - y] == "Miami Heat" or teams[4 - y] == "Phoenix Suns":
        oppPower = 7
    elif teams[4 - y] == "LA Lakers" or teams[4 - y] == "Dallas Mavericks":
        oppPower = 6
    elif teams[4 - y] == "Chicago Bulls":
        oppPower = 5
    if power - oppPower == 1 or power - oppPower == 2 or power - oppPower == 3:
        print("Your team has an advantage over the opposing team.")
    elif power - oppPower == 0:
        print("Your teams are equally matched.")
    elif power - oppPower == -1 or power - oppPower == -2 or power - oppPower == -3:
        print("The opposing team has an advantage over your team.")
    while (b == False):
        if random.randint(1, power) >= random.randint(1, oppPower):
            print("You won a game!")
            secondRoundRecord[0] += 1
            print("The record is,", secondRoundRecord[0], "-", secondRoundRecord[1])
            print("Since you won, your coach instructed you to rest up for the next game.")
        else:
            print("You lost a game.")
            secondRoundRecord[1] += 1
            print("The record is,", secondRoundRecord[0], "-", secondRoundRecord[1])
            print("Since you lost, your coach has told you to rest up or practice, its up to you.")
            print("1: Rest")
            print("2: Train")
            choice = input()
            if choice == 1:
                print(
                    "You chose to rest instead of training for the next game, hopefully this doesn't impact your gameplay.")
            elif choice == 2:
                print("You chose to go to a training session and brought your team along as well.")
                power += 1
        if secondRoundRecord[0] == 4:
            b = True
            print("You won your second round series!")
            finals()
        elif secondRoundRecord[1] == 4:
            b = True
            print("You lost in the second round and are now going to Cancun.")
            print("Cancun was nice, and now your gonna play another season.")
            nextSeason()


def finals():
    global teams, yourTeam, power, oppPower, finalsRecord, c, rings
    y = teams.index(yourTeam) + 1
    matchups = [[teams[0], teams[3]], [teams[1], teams[2]]]
    for matchup in matchups:
        if yourTeam not in matchup:
            if getTeamPower(matchup[0]) < getTeamPower(matchup[1]):
                weakerTeam = matchup[0]
            else:
                weakerTeam = matchup[1]
            teams.remove(weakerTeam)
    if y == 1:
        teams.remove(matchups[0][1])
    elif y == 4:
        teams.remove(matchups[0][0])
    elif y == 2:
        teams.remove(matchups[1][1])
    elif y == 3:
        teams.remove(matchups[1][0])
    finalsTable = PrettyTable(["Seed", "Teams"])
    for i in range(len(teams)):
        finalsTable.add_row(
            [i + 1, teams[i]])
    print(finalsTable)
    y = teams.index(yourTeam) + 1
    print("Your team the,", yourTeam, "will play against the", teams[2 - y], "in a 7 game series.")
    if yourTeam == "Boston Celtics" or yourTeam == "Milwaukee Bucks" or yourTeam == "Golden State Warriors":
        power = 8
    elif yourTeam == "Miami Heat" or yourTeam == "Phoenix Suns":
        power = 7
    elif yourTeam == "LA Lakers" or yourTeam == "Dallas Mavericks":
        power = 6
    elif yourTeam == "Chicago Bulls":
        power = 5
    if teams[2 - y] == "Boston Celtics" or teams[2 - y] == "Milwaukee Bucks" or teams[2 - y] == "Golden State Warriors":
        oppPower = 8
    elif teams[2 - y] == "Miami Heat" or teams[2 - y] == "Phoenix Suns":
        oppPower = 7
    elif teams[2 - y] == "LA Lakers" or teams[2 - y] == "Dallas Mavericks":
        oppPower = 6
    elif teams[2 - y] == "Chicago Bulls":
        oppPower = 5
    if power - oppPower == 1 or power - oppPower == 2 or power - oppPower == 3:
        print("Your team has an advantage over the opposing team.")
    elif power - oppPower == 0:
        print("Your teams are equally matched.")
    elif power - oppPower == -1 or power - oppPower == -2 or power - oppPower == -3:
        print("The opposing team has an advantage over your team.")
    while (c == False):
        if random.randint(1, power) >= random.randint(1, oppPower):
            print("You won a game!")
            finalsRecord[0] += 1
            print("The record is,", finalsRecord[0], "-", finalsRecord[1])
            print("Since you won, your coach instructed you to rest up for the next game.")
        else:
            print("You lost a game.")
            finalsRecord[1] += 1
            print("The record is,", finalsRecord[0], "-", finalsRecord[1])
            print("Since you lost, your coach has told you to rest up or practice, its up to you.")
            print("1: Rest")
            print("2: Train")
            choice = input()
            if choice == 1:
                print(
                    "You chose to rest instead of training for the next game, hopefully this doesn't impact your gameplay.")
            elif choice == 2:
                print("You chose to go to a training session and brought your team along as well.")
                power += 1
        if finalsRecord[0] == 4:
            c = True
            print("You won the finals!")
            rings += 1
            win()
        elif finalsRecord[1] == 4:
            c = True
            print("You lost in the finals and are now going to Cancun.")
            print("Cancun was nice, and now your gonna play another season.")
            nextSeason()


def win():
    global seasons, rings
    print("The", yourTeam, "have won a championship while you were playing!")
    if rings == 1:
        print("It took you", seasons, "seasons to get your first ring.")
        print("Do you want to continue playing in the NBA? y/n")
        choice = input()
        if choice == "y":
            nextSeason()
        elif choice == "n":
            end()
    else:
        print("This is your", seasons, "season in the NBA.")
        print("Do you want to continue playing in the NBA? y/n")
        choice2 = input()
        if choice2 == "y":
            nextSeason()
        elif choice2 == "n":
            end()


def end():
    print("You chose to not play in the NBA anymore, and to retire after a championship win.")
    print("Your accolades are:")
    print("Seasons:", seasons)
    print("Rings:", rings)
    print("Although this is the end of your NBA career, you will prosper in other aspects of your life.")


def seasonEnd():
    print("Unfortunately, you have gotten too old to continue playing in the NBA.")
    print("You decide to retire after an illustrious career, and put the rest of your time and effort into something else.")
    print("Your accolades are:")
    print("Seasons:", seasons)
    print("Rings:", rings)


def nextSeason():
    global teams, yourTeam, a, b, c, firstRoundRecord, secondRoundRecord, finalsRecord, seasons
    seasons += 1
    if seasons >= 20:
        seasonEnd()
    else:
        print("The playoff bracket is as follows:")
        teams = ["Boston Celtics", "Milwaukee Bucks", "Chicago Bulls", "Miami Heat", "Phoenix Suns",
                 "Golden State Warriors", "LA Lakers", "Dallas Mavericks"]
        random.shuffle(teams)
        playoffTable = PrettyTable(["Seed", "Teams"])
        for i in range(len(teams)):
            playoffTable.add_row(
                [i + 1, teams[i]])
        print(playoffTable)
        y = teams.index(yourTeam) + 1
        print("Your team, the", yourTeam, "were the", y, "seed.")
        print("The team that you will play against is the", 9 - y, "seeded", teams[8 - y], "in a 7 game series.")
        firstRoundRecord = [0, 0]
        secondRoundRecord = [0, 0]
        finalsRecord = [0, 0]
        a = False
        b = False
        c = False
        firstRound()


def getTeamPower(team):
    if team == "Boston Celtics" or team == "Milwaukee Bucks" or team == "Golden State Warriors":
        return 8
    elif team == "Miami Heat" or team == "Phoenix Suns":
        return 7
    elif team == "LA Lakers" or team == "Dallas Mavericks":
        return 6
    elif team == "Chicago Bulls":
        return 5


def main():
    start()


main()

