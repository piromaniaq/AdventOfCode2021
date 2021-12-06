bingoInput = []

with open('day4.txt') as f:
    lines = f.readlines()
    for line in lines:
        bingoInput.append(line.strip())

bingoNumbers = [int(x) for x in bingoInput[0].split(',')]
bingoTable = []

for i in range((len(bingoInput) // 6)):
    temporaryTable = []
    for j in range(5):
        temporaryTable.append([int(x) for x in bingoInput[(i * 6) + 2 + j].split()])  # +2 because first two rows are useless
    bingoTable.append(temporaryTable)

def checkNumber(table, number):
    for x in table:
        for y, verificatior in enumerate(line):
            if verificatior == number:
                line[y] = -1
    return table

def checkWin(table):
    for row in table:
        if sum(row) == -5:
            return True
        for x in range(5):
            columnSum = 0
            for y in range(5):
                columnSum += table[x][y]
            if columnSum == -5:
                return True
        else:
            return False