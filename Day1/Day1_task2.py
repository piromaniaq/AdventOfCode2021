depths = []
trios = []

with open('sonar.txt') as f:
    lines = f.readlines()
    for line in lines:
        depths.append(int(line.strip()))

for depth in range(len(depths) - 2):
    triosSums = depths[depth] + depths[depth + 1] + depths[depth + 2]
    trios.append(triosSums)

firstTrio = True
oldTrio = 0
increaseCounter = 0

for trio in trios:
    if firstTrio:
        oldTrio = trio
        firstTrio = False

    diffTrio = trio - oldTrio
    oldTrio = trio

    if diffTrio > 0:
        increaseCounter += 1

print(increaseCounter)