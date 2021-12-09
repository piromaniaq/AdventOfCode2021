daysNumber = 80
oldDaysFirst = []

with open('day6.txt') as f:
    lines = f.readlines()
    for line in lines:
        oldDaysFirst.append(line.strip())

oldDays = [int(x) for x in oldDaysFirst[0].split(',')]
newFish = 8


def next_day(y):
    for x in range(len(oldDays)):
        if oldDays[x] > 0:
            oldDays[x] = oldDays[x] - 1
        elif oldDays[x] == 0:
            oldDays[x] = 6
            oldDays.append(newFish)
    return oldDays


for x in range(daysNumber):
    next_day(x)

print(len(oldDays))