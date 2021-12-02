depths = []


with open('sonar.txt') as f:
    lines = f.readlines()
    for line in lines:
        depths.append(int(line.strip()))


firstDepth = True
currentDepth = 0
increaseCounter = 0

for depth in depths:
    if firstDepth:
        currentDepth = depth
        firstDepth = False

    diffDepth = currentDepth - depth
    currentDepth = depth

    if diffDepth < 0:
        increaseCounter += 1

print(increaseCounter)
