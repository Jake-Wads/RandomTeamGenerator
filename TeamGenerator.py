groupNum = 3

def printLists(teamList):
    teamNum = len(teamList)
    teamSize = len(teamList[0])
    for i in range(0, teamNum):
        print("Team " + str(i+1) + ":")
        for j in range(0, teamSize):
            print(teamList[i][j])

def getTestInputList():
    
    print("How many teams?")
    teamNum = int(input())
    print("People per team?")
    teamSize = int(input())

    teamList = [[0 for x in range(teamSize)] for y in range(teamNum)] 

    for i in range(0, teamNum):
        for j in range(0, teamSize):
            print("Team " + str(i+1) + ", Person " + str(j+1) + ":")
            teamList[i][j] = input()

    return teamList

def main():
    print("Hello World!")
    teamList = getTestInputList()
    printLists(teamList)

main()