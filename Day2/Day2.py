moves = []

with open('move.txt') as f:
    lines = f.readlines()
    for line in lines:
        moves.append(line.strip())

forward = 0
depth = 0

for move in moves:
    splitMoves = move.split()
    splitMoves[1] = int(splitMoves[1])

    match splitMoves[0]:
        case 'forward':
            forward += splitMoves[1]
        case 'up':
            depth -= splitMoves[1]
        case 'down':
            depth += splitMoves[1]

result = forward * depth
print(result)

