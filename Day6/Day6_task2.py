daysNumber = 256
oldDaysFirst = []

with open('day6.txt') as f:
    lines = f.readlines()
    for line in lines:
        oldDaysFirst.append(line.strip())

oldDays = [int(x) for x in oldDaysFirst[0].split(',')]


if __name__ == '__main__':
    result = []
    counter = 0
    for x in range(9):
        result.append(oldDays.count(x))
    while counter < daysNumber + 1:
        print(counter, sum(result), result)
        tempCounter = result[0]
        del result[0]
        result[6] += tempCounter
        result.append(tempCounter)
        counter += 1

