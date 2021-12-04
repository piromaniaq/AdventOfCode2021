reports = []

with open('data.txt') as f:
    lines = f.readlines()
    for line in lines:
        reports.append(line.strip())

gammaRate = ''
epsilonRate = ''

for i in range(0, len(reports[0])):
    checkValue = 0
    for report in reports:
        if report[i] == '1':
            checkValue += 1
        else:
            checkValue -= 1
    if checkValue > 0:
        gammaRate += '1'
        epsilonRate += '0'
    else:
        gammaRate += '0'
        epsilonRate += '1'

print(int(gammaRate, 2) * int(epsilonRate, 2))
