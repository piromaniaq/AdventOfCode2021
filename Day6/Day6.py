oldDays = []

with open('day6_test.txt') as f:
    lines = f.readlines()
    for line in lines:
        oldDays.append(line.strip())

oldDaysList = [int(x) for x in oldDays[0].split(',')]

print(oldDays)
print(oldDaysList)