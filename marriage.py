import sys
# get the argument, make sure the file name is correctly formatted
def getFile():
    return open(sys.argv[1])

knightDict = dict()
ladyDict = dict()
freeKnights = []
couplesKL = dict()
couplesLK = dict()
# for every line of the file except the first one, there is a name of a person followed his/her ranking of the opposite gender population of the kingdom in decreasing order, the first one being the favorite.
# for every knight there is a dictionary containing the name of the knight as a string key and a list of string lady names as the value. 
# for every lady there is a dictionary containing the name of the lady as a string key and a list of string knight names as the value. 
def getKingdomAndRanking(file):
    for idx, line in enumerate(file):
        lineNames = line.split()
        if idx == 0:
            try: numKnight = int(line) # for every file, for every first line the is n which is the number of knights and ladies
            except: exit(1)
        else:
            if idx <= numKnight: 
                knightName = lineNames.pop(0)
                knightDict[knightName] = lineNames

            else:
                ladyName = lineNames.pop(0)
                ladyDict[ladyName] = lineNames
    return numKnight

# for every free knight in the kingdom there is a lady to propose that hasn't rejected the knight and is the knight's current favorite. (pigonHole)
    # for every free lady proposed there is a "maybe" couple formed
    # for every taken lady there is a knight partner decision to make depending on the lady's ranking
    # for 'losers' (knights rejected) there is a new proposal to make
        # # the number of free knight does not increase, the number of free women does not decrease. 
        # # so that the algorithm can reach termination
# once there is no more free knights (losers) there is a stable configuration of couples within the kingdom
# there is no knight and lady who would both prefer each other over their current partner

def makeCouples():
    freeKnights = list(knightDict.keys())

    while freeKnights:
        knightName = freeKnights[0]
        favLadyName = knightDict[knightName][0]
        favLadyRank = ladyDict[favLadyName]
        
        if favLadyName not in couplesLK.keys(): 
            couplesKL[knightName] = favLadyName
            couplesLK[favLadyName] = knightName
            freeKnights.pop(0)
    
        elif favLadyRank.index(knightName) < favLadyRank.index(couplesLK[favLadyName]):
            loserKnightName = couplesLK[favLadyName]
            freeKnights.append(loserKnightName)
            del couplesKL[loserKnightName]
            knightDict[loserKnightName].pop(0)
            del couplesLK[favLadyName]
            couplesKL[knightName] = favLadyName
            couplesLK[favLadyName] = knightName
            freeKnights.pop(0)
        else:
            knightDict[knightName].pop(0)
def printCouplesKL():
    getKingdomAndRanking(getFile())
    makeCouples()
    for knight, lady in couplesKL.items(): print(knight, lady) # for every stable couple there is a line to print on STDOUTPUT
    
try:
    printCouplesKL()
except: exit(1)