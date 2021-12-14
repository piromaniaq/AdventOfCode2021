import collections


def get_data(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
    return data


def position(data):
    points: collections.Counter[tuple[int, int]] = collections.Counter()
    counter = 0
    for line in data:
        start, end = line.split(' -> ')
        x1_s, y1_s = start.split(',')
        x2_s, y2_s = end.split(',')
        x1, y1, x2, y2 = int(x1_s), int(y1_s), int(x2_s), int(y2_s)

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)):
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)):
                points[(x, y1)] += 1
    for k, v in points.most_common():
        if v > 1:
            counter += 1
        else:
            break
    return  counter


if __name__ == '__main__':
    data = get_data('input.txt')
    result = position(data)
    print(result)