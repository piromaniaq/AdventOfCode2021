moves = []

with open('move.txt') as f:
    lines = f.readlines()
    for line in lines:
        moves.append(line.strip())


horizontal = 0
depth = 0
aim = 0

for move in moves:
    splitMoves = move.split()
    splitMoves[1] = int(splitMoves[1])

    match splitMoves[0]:
        case 'forward':
            horizontal += splitMoves[1]
            depth += aim * splitMoves[1]
        case 'down':
            aim += splitMoves[1]
        case 'up':
            aim -= splitMoves[1]

result = horizontal * depth
print(result)