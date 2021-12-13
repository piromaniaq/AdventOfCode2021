def get_data(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
        dataSplit = [int(x) for x in data[0].split(',')]
    return dataSplit


def check_position(data):
    minPosition = min(data)
    maxPosition = max(data)
    map = {}
    for x in range(maxPosition - minPosition + 1):
        fuel = 0
        for y in range(len(data)):
            fuel += abs(x - data[y])
        map[x] = fuel
    minFuelUsage = 99999999
    for k, l in map.items():
        if l <= minFuelUsage:
            minFuelUsage = l
    return minFuelUsage


if __name__ == '__main__':
    input = get_data('input.txt')
    print(check_position(input))
