bingoInput = []

with open('day4.txt') as f:
    lines = f.readlines()
    for line in lines:
        bingoInput.append(line.strip())

bingoNumbers = [int(x) for x in bingoInput[0].split(',')]
print(bingoNumbers)
