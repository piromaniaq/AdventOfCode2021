bingoInput = []

with open('day4.txt') as f:
    lines = f.readlines()
    for line in lines:
        bingoInput.append(line.strip())

bingoNumbers = [int(x) for x in bingoInput[0].split(',')]
bingoTables = []

for i in range((len(bingoInput) // 6)):
    temporaryTable = []
    for j in range(5):
        temporaryTable.append([int(x) for x in bingoInput[(i * 6) + 2 + j].split()])
        # +2 because first two rows are useless
    bingoTables.append(temporaryTable)


def checkNumber(table, number):
    for line in table:
        for j, spot in enumerate(line):
            if spot == number:
                line[j] = -1
    return table


def checkWin(table):
    for row in table:
        if sum(row) == -5:
            return True
        for i in range(5):
            columnSum = 0
            for j in range(5):
                columnSum += table[j][i]
            if columnSum == -5:
                return True
        else:
            return False


def sumWinner(table):
    totalSum = 0
    for line in table:
        for spot in line:
            if spot != -1:
                totalSum += spot
    return totalSum


def playBingo(bingoTables, bingoNumbers):
    checkedBingoTables = bingoTables
    winnerBingo = []

    for j, bingoDraw in enumerate(bingoNumbers):
        if len(checkedBingoTables) > 0:
            newCheckedBingoTables = []
            for table in checkedBingoTables:
                checkNumber(table, bingoDraw)
                if checkWin(table):
                    print('We have a winner!')
                    winnerBingo.append(table)
                else:
                    print('Try again!')
                    newCheckedBingoTables.append(table)
            checkedBingoTables = newCheckedBingoTables
        else:
            print('Quit')
            print(checkedBingoTables)
            return winnerBingo, bingoNumbers[j-1]


winnerBingo = playBingo(bingoTables, bingoNumbers)
winnerTable = winnerBingo[0][-1]
print(f'Card: {winnerTable}')
winnerDraw = winnerBingo[1]
print(f'Draw: {winnerDraw}')

result = sumWinner(winnerTable) * winnerDraw
print(result)