import re
from Classes.Moneyline import PremierLeague

def FanDuelParser():
    file = open("data/PLOddsFanDuel.txt")
    lines = file.readlines()
    index = 0
    current = 0
    naughtindex = []
    moneylineList = []

    for i in lines:
        if current + 2 < index and re.search("^([+]|[-])", i) != None:
            current = index
            naughtindex.append(index)
        index += 1

    for i in naughtindex:
        moneyline = PremierLeague(
            lines[i-2][:-1] if lines[i-1][:-1] != '0' else lines[i-4][:-1],
            lines[i-1][:-1] if lines[i-1][:-1] != '0' else lines[i-2][:-1], 
            lines[i][:-1], 
            lines[i+1][:-1], 
            lines[i+2][:-1])
        
        moneylineList.append(moneyline)

    return moneylineList